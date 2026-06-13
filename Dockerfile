# استخدام نسخة خفيفة ومستقرة من بايثون
FROM python:3.11-slim

# تحديث النظام وتثبيت بعض الحزم الأساسية التي قد يحتاجها dbt للعمل بسلاسة
RUN apt-get update -y && \
    apt-get install --no-install-recommends -y -q \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# تحديد مسار العمل داخل الحاوية ليتطابق مع ما حددناه في docker-compose
WORKDIR /usr/app/project_dbt

# تحديث pip وتثبيت محول dbt الخاص بـ Snowflake
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir dbt-snowflake

# أمر افتراضي للتحقق من التثبيت (سيتم تجاوزه بواسطة docker-compose)
CMD ["dbt", "--version"]