import wikipediaapi
import json


def get_wikipedia_text(title, lang="fa"):
    """ دریافت متن مقاله ویکی‌پدیا بر اساس عنوان """
    wiki = wikipediaapi.Wikipedia(
        language=lang,
        user_agent="MyWikipediaScraper/1.0 (contact: example@email.com)"
    )

    page = wiki.page(title)

    if not page.exists():
        print(f"⚠️ صفحه '{title}' یافت نشد!")
        return None

    return {"title": title, "text": page.text}


def create_wikipedia_dataset(titles, output_file="dataset.json", lang="fa"):
    """ دریافت مقالات و ذخیره در قالب JSON """
    dataset = []

    for title in titles:
        data = get_wikipedia_text(title, lang)
        if data:
            dataset.append(data)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(dataset, f, ensure_ascii=False, indent=4)

    print(f"✅ دیتاست در فایل '{output_file}' ذخیره شد.")


# لیست مقالات ویکی‌پدیا برای ساخت دیتاست
titles_list = ["هوش_مصنوعی", "یادگیری_ماشین", "پردازش_زبان‌های_طبیعی", "شبکه_عصبی_مصنوعی"]

# اجرای تابع و ساخت دیتاست
create_wikipedia_dataset(titles_list)
