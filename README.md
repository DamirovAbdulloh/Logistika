# Logistika UZ — v8

Django-da yozilgan logistika boshqaruv tizimi.

## O'zgarishlar (v8)
- ✅ **PostgreSQL** — SQLite o'rniga PostgreSQL ishlatiladi (Render/Railway uchun tayyor)
- ✅ **Responsive dizayn** — Mobile sidebar, burger menu
- ✅ **data.py** — haqiqiy ma'lumotlar (haydovchilar, putyovka, TIR, dazvol, ijara, chiqimlar) bilan to'ldirilgan import skripti

---

## Lokal ishga tushirish (SQLite bilan, tezkor test uchun)

```bash
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt

python manage.py migrate
python data.py                    # haqiqiy ma'lumotlarni import qiladi
python manage.py createsuperuser  # admin login uchun (Django auth user)
python manage.py runserver
```

`DATABASE_URL` muhit o'zgaruvchisi berilmagan bo'lsa, loyiha avtomatik SQLite (`db.sqlite3`) bilan ishlaydi — `logistika/settings.py` shunday sozlangan.

---

## Render.com'ga deploy qilish (PostgreSQL bilan)

### 1. GitHub'ga joylash
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <repo-url>
git push -u origin main
```
`db.sqlite3` va `venv/` `.gitignore` orqali repога tushmaydi — bu to'g'ri, chunki production'da PostgreSQL ishlatiladi.

### 2. Render.com'da PostgreSQL yaratish
- Render dashboard → **New** → **PostgreSQL** → nom bering → **Create Database**
- Yaratilgandan so'ng **Internal Database URL**ni nusxalab oling

### 3. Render.com'da Web Service yaratish
- **New** → **Web Service** → GitHub repongizni tanlang
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn logistika.wsgi --log-file -` (Procfile orqali avtomatik aniqlanadi)
- **Environment Variables** bo'limida quyidagilarni qo'shing:
  | Key | Value |
  |-----|-------|
  | `DATABASE_URL` | (2-qadamdagi Internal Database URL) |
  | `SECRET_KEY` | tasodifiy uzun maxfiy satr |
  | `DEBUG` | `False` |
  | `ALLOWED_HOSTS` | `your-app.onrender.com` |

### 4. Deploy bo'lgandan so'ng — migratsiya va ma'lumotlarni import qilish
Render dashboard → Web Service → **Shell** bo'limini ochib:
```bash
python manage.py migrate
python data.py                    # haqiqiy ma'lumotlarni PostgreSQL'ga import qiladi
python manage.py createsuperuser  # admin panel uchun login yaratish
```

`data.py` ichidagi barcha import funksiyalari `get_or_create` mantig'ida yozilgan — skript necha marta ishga tushirilsa ham, takror yozuvlar yaratilmaydi.

---

## Mavjud sahifalar
| Sahifa | URL |
|--------|-----|
| Login | `/` |
| Dashboard | `/admin/` |
| Haydovchilar | `/admin/drivers/` |
| Putyovkalar | `/admin/putyovkalar/` |
| TIRlar | `/admin/tirlar/` |
| Dazvollar | `/admin/dazvollar/` |
| Litsenziyalar | `/admin/litsenziyalar/` |
| Ijara | `/admin/ijara/` |
| Chiqimlar | `/admin/chiqimlar/` |
