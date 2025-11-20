# 13. Napisz program który z dowolnej strony WWW przeczyta wszystkie obrazki
#     zmniejszy je do szerokości 320px (z zachowaniem proporcji jeśli chodzi o wysokość) i wyśle w mailu jako załączniki (a może nawet jako plik ZIP?). W treści maila niech będzie lista plików
#     z informacją z jakiego rozmiaru zostały zmniejszone/zwiększone i jaki był zysk/strata jeśli chodzi o rozmiar poszczególnego pliku jak i sumarycznie wszystkich.

import os
import requests
from bs4 import BeautifulSoup
from PIL import Image
import zipfile
import smtplib

from urllib.parse import urljoin

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


# ======== USTAWIENIA SMTP ========
SMTP_SERVER = "smtp.interia.pl"
SMTP_PORT = 465
SMTP_USER = "test_python@interia.pl"
SMTP_PASSWORD = "testpython12345!"

FROM_EMAIL = SMTP_USER


# ===========================================================================================
# ---------- Funkcje do ściągania obrazków ---------
# ===========================================================================================

# przykładowy adres strony: https://www.olx.pl/motoryzacja/samochody/
# można by dopisać to do defaulta w celach testowych, ale ogólnie defaultowy link nie ma za bardzo sensu


def find_image_urls(page_url: str) -> list[str]:
    print("Pobieram HTML strony...")
    response = requests.get(page_url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")

    image_urls: list[str] = []

    for img in soup.find_all("img"):
        src = img.get("src")
        if not src:
            continue

        full_url = urljoin(page_url, src)

        # pomijamy tylko data: (inline base64), bo z tym jest zabawa
        if full_url.startswith("data:"):
            continue

        image_urls.append(full_url)

    # usuwamy duplikaty (jakby ten sam obrazek pojawił się kilka razy), zachowując oryginalną kolejność
    # dict.fromkeys tworzy nowy słownik
    # przechodzimy po każdym elemencie listy i zapisujemy go jako klucz (nie może być zduplikowany!) i None jako wartość
    # jeśli jest coś zduplikowane to Python to nadpisuje (np. jakby były 2x 1.jpg to zostanie tylko ten ostatni)
    # list zwraca listę kluczy (słownik iteruje tylko po kluczach)
    image_urls = list(dict.fromkeys(image_urls))

    print(f"Znaleziono {len(image_urls)} potencjalnych obrazków.")
    return image_urls


def download_images(urls: list[str], folder: str) -> list[str]:
    """Pobieranie obrazków na dysk."""
    os.makedirs(folder, exist_ok=True)
    saved_files = []

    for i, url in enumerate(urls, start=1):
        try:
            print(f"Pobieram: {url}")
            resp = requests.get(url, timeout=10)
            resp.raise_for_status() # żeby zwrócić kod błędu i przejść do except

            content_type = resp.headers.get("Content-Type", "") # robimy to żeby się upewnić, że faktycznie mamy obrazek; tego nie widać w HTMLu (HTML deklaruje: „to obrazek”, HTTP Content-Type faktycznie pokazuje, co tam jest)

            if "svg" in content_type: # pomijamy SVG, bo PIL nie umie tego otworzyć
                print("Pomijam SVG:", url)
                continue

            if not content_type.startswith("image/"):
                print(f"Oszustwo! To nie jest obrazek ({content_type}. Pomijam!)")
                continue

            # wybieramy rozszerzenie na podstawie Content-Type
            if "png" in content_type:
                ext = ".png"
            else:
                ext = ".jpg"

            filename = f"img_{i}{ext}"
            path = os.path.join(folder, filename)

            with open(path, "wb") as f:
                f.write(resp.content)

            saved_files.append(path)

        except Exception as e:
            print(f"  Błąd pobierania {url}: {e}")

    print(f"Pobrano {len(saved_files)} obrazków.")
    return saved_files


# ===========================================================================================
# ---------- Funkcja do zmniejszania obrazków ----------
# ===========================================================================================

def resize_images(files: list[str], folder: str) -> list[str]:
    """Zmniejsza obrazki do zadanej wielkości (tu szerokość 320px)."""
    os.makedirs(folder, exist_ok=True)
    resized = []

    for filepath in files:
        try:
            img = Image.open(filepath)
            w, h = img.size

            new_w = 320
            new_h = int(h * (new_w / w))

            img = img.resize((new_w, new_h))

            filename = os.path.basename(filepath)
            new_path = os.path.join(folder, filename)

            img.save(new_path)

            resized.append(new_path)

        except Exception as e:
            print(f"Nie mogę zmniejszyć {filepath}: {e}")

    return resized


# ===========================================================================================
# ---------- Funkcje do wysyłania obrazków ----------
# ===========================================================================================

def make_zip(files: list[str], zip_name="images.zip") -> str:
    """Pakowanie obrazków do ZIPa."""
    with zipfile.ZipFile(zip_name, "w") as z:
        for f in files:
            z.write(f, os.path.basename(f)) # basename wyciąga samą nazwę pliku bez ścieżki
    return zip_name


def send_mail(to_email: str, subject: str, body: str, attachment_path: str) -> None:
    """Wysyła e-mail z załącznikiem ZIP."""
    try:
        msg = MIMEMultipart() # tworzymy obiekt klasy MIMEMultipart(); może zawierać treść, załącznik, HTMLa itp.
        msg["From"] = SMTP_USER
        msg["To"] = to_email
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "plain", "utf-8")) # dodawanie treści wiadomości (zwykły, prosty tekst z utf-8 żeby działały polske znaki)

        # Dodawanie załącznika
        with open(attachment_path, "rb") as f: # otwieramy plik do załaczenia - u nas zip
            part = MIMEBase("application", "zip") # mówimy, że ta część maila to ZIP (application - dane binarne, nie tekst ani obrazek)
            part.set_payload(f.read()) # f.read() czyta całą zawartość pliku; set_payload ustawia to co wczytane jako load do wiadomości (czyli umieszczamy surowego ZIPa/bajty tutaj)
            encoders.encode_base64(part) # kodowanie payloadu z bajtów na Base64 (bezpieczny tekst) żeby dało się go bezpiecznie wysłać w mailu (maile są historycznie tekstowe)
            part.add_header(
                "Content-Disposition", # pole w nagłówku, który mówi klientowi pocztowemu jak traktować tę część maila
                f'attachment; filename="{os.path.basename(attachment_path)}"' # mówimy, że to załącznik i ma się nazywać tak jak nazwa pliku (bez reszty ścieżki)
            )
            msg.attach(part)

        print("\nPróbuję wysłać maila...")

        # próba połączenia i wysyłki
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, timeout=15) as smtp: #tworzymy nowe połączenie z serwerem
            # Logowanie (podając login i hasło)
            smtp.login(SMTP_USER, SMTP_PASSWORD)
            # Wysyłąnie maila
            smtp.sendmail(SMTP_USER, to_email, msg.as_string())

        print("\nMail wysłany poprawnie!")

    except smtplib.SMTPAuthenticationError:
        print("\nBłąd logowania do skrzynki pocztowej. Sprawdź login i hasło SMTP.")
    except smtplib.SMTPConnectError:
        print("\nNie udało się połączyć z serwerem SMTP.")
    except smtplib.SMTPException as e:
        print(f"\nOgólny błąd SMTP: {e}")
    except FileNotFoundError:
        print("\nZałącznik nie istnieje – nie można wysłać maila.")
    except Exception as e:
        print(f"\nNieznany błąd podczas wysyłania maila: {e}")


# ===========================================================================================
# ---------- FUNKCJA GŁÓWNA (obsługa wejścia i logika programu) ----------
# ===========================================================================================

def main():
    page = input("Podaj adres strony: ").strip()
    email = input("Na jaki adres wysłać ZIP? ").strip()

    print("\n------ START ------")
    urls = find_image_urls(page)

    print("\nPobieram obrazki...")
    downloaded = download_images(urls, "oryginalne")

    print("\nZmniejszam obrazki...")
    small = resize_images(downloaded, "320px")

    print("\nPakuję ZIP...")
    zip_path = make_zip(small)

    send_mail(email, "Obrazki 320px", "Obrazki w załączniku :)", zip_path)


if __name__ == "__main__":
    main()