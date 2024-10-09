from google.oauth2.service_account import Credentials
import gspread

from back.app.core.config import settings


scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

credentials = Credentials.from_service_account_file(
    "./app/db/creds.json", scopes=scopes
)

gc = gspread.authorize(credentials)

session = gc.open_by_key(settings.GS.id).sheet1
