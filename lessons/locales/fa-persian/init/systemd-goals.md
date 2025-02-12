# اهداف Systemd

## محتوای درس

ما به جزئیات نوشتن فایل‌های unit نمی‌پردازیم. ولی نگاهی جزئی به ساختار آن‌ها و
روش‌های کنترل دستی‌شان خواهیم پرداخت.

در این‌جا یک فایل unit برای سرویسی به اسم foobar.service را مشاهده می‌کنید

```
[Unit]
Description=My Foobar
Before=bar.target

[Service]
ExecStart=/usr/bin/foobar

[Install]
WantedBy=multi-user.target
```

این unit بسیار ساده است‌، در شروع فایل بخشی به اسم [unit] را مشاهده می‌کنید. این
بخش به ما امکان تعریف توضیحات و چیدمان اجرای unit را می‌دهد. بخش بعدی‌، [Service]
چگونگی شروع، پایان و بارگذاری مجدد سرویس را نشان می‌دهد. و در آخر بخش [Install]
برای مدیریت نیازمندی‌ها استفاده شده است. این تنها مشتی نمونهٔ خروار از امکانات
موجود برای توسعهٔ یک فایل systemd است. می‌توانید برای کشف جزئیات بیشتر در موردش روی
اینترنت منابع بیشتری پیدا کیند.

حالا بیایید به چند دستور که می‌توانید با systemd استفاده‌اش کنیم بپردازیم:

### لیست کردن unit‌ها

```
$ systemctl list-units
```

### مشاهده وضعیت unit‌ها

```
$ systemctl status networking.service
```

### شروع یک سرویس

```
$ sudo systemctl start networking.service
```

### متوقف کردن یک سرویس

```
$ sudo systemctl stop networking.service
```

### اجرای مجدد یک سرویس

```
$ sudo systemctl restart networking.service
```

### فعال کردن یک unit

```
$ sudo systemctl enable networking.service
```

### غیرفعال کردن یک unit


```
$ sudo systemctl disable networking.service
```

تکرار می‌کنم‌، برای دیدن عمق امکانات systemd‌، بهتر است منابع بیشتری در خصوصش مطالعه کنید.


## تمرینات

وضعیت سرویس‌های روی سیستم‌تان را بررسی کنید و چند‌تایی را شروع یا متوقف کنید. چه چیزی مشاهده می‌کنید؟

### سوالات آزمون

دستور شروع برای سرویسی به اسم peanut.service چیست؟

```
sudo systemctl start peanut.service
```
