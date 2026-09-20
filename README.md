# architect_effects

Architect Effects için geliştirilen yapay zekâ destekli müşteri iletişim ve lead toplama uygulamasıdır.

## Proje Hakkında

Architect Effects, iç mimar Esra Tekerlekçi tarafından oluşturulan, ev dekorasyonu ve duvar sanatı alanında faaliyet gösteren bir markadır.

Marka; canvas tablolar ve dijital tasarımlar sunmaktadır. Tasarım anlayışında Japandi, Bauhaus, mid-century ve minimalist stillerden yararlanılmaktadır.

Bu projede amaç, Architect Effects web sitesini ziyaret eden kullanıcıların yapay zekâ destekli bir sohbet alanı üzerinden bilgi alabilmesi ve potansiyel müşterilerin iletişim bilgilerinin lead olarak toplanabilmesidir.

Toplanan lead bilgileri işletme sahibi tarafından dashboard üzerinden görüntülenebilecektir.

## Projenin Amaçları

- Ziyaretçilerle yapay zekâ destekli sohbet gerçekleştirmek
- Kullanıcılardan isim, telefon ve mesaj bilgilerini almak
- Lead kayıtlarını veritabanında saklamak
- Lead kayıtlarını dashboard üzerinden görüntülemek
- Frontend ve backend arasında API tabanlı iletişim sağlamak
- Uygulamayı GitHub ve Render üzerinden yayınlanabilir hale getirmek

## Kullanılan Teknolojiler

- Python
- Flask
- SQLite
- Flask-CORS
- Requests
- Python-dotenv
- Groq API
- HTML
- CSS
- JavaScript
- Wix Velo
- Git
- GitHub
- Render

## Proje Mimarisi

```text
architect_effects/
├── run.py
├── config.py
├── requirements.txt
├── .env
├── .gitignore
└── app/
    ├── __init__.py
    ├── database.py
    ├── routes.py
    ├── templates/
    │   ├── index.html
    │   └── dashboard.html
    └── services/
        ├── __init__.py
        └── ai_service.py