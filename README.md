<!-- ABOUT THE PROJECT -->
## اسکرین شات از برنامهٔ اجرا شده

![اسکرین شات](https://user-images.githubusercontent.com/51531010/208266235-f50d1399-8e15-4338-a16b-5a41408903f0.jpg)

توضیحات:
* در صورتی که بخواهید یکی از چت‌های تلگرام‌تون رو آنالیز کنید و نمودار میزان چت کردن از ابتدای چت به تفکیک هر ماه را بصورت نمودار ببینید می‌توانید از این اسکریپت استفاده کنید

### نصب پیش‌نیازها

با کمک دستور زیر می‌توانید محتوای داخل requirements را نصب کنید
  ```sh
  pip install -r requirements.txt
  ```

### نحوه استفاده

* ابتدا با استفاده از گزینهٔ Chat Export تلگرام، یک خروجی از چت مورد نظر بگیرید. دقت کنید که حتما بصورت Machine Readable (JSON) خروجی بگیرید. (فقط در Telegram Desktop در دسترس است.)
* خروجی مورد نظر را با اسم result.json ذخیره کنید و کنار فایل script.py در یک فولدر قرار دهید
* فایل script.py را ران کنید و منتظر بمانید تا برنامه بصورت کامل اجرا شود
