
#!/bin/bash

# معلومات الدخول
USERNAME="rat1001rat-dev"
TOKEN="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"

# رابط المستودع الجديد
REPO="github.com/rat1001rat-dev/mila.git"

# تغيير عنوان الريموت إلى عنوان يتضمن التوكن
git remote set-url origin https://$USERNAME:$TOKEN@$REPO

# التأكد من أن الفرع اسمه main
git branch -M main

# دفع الملفات إلى المستودع الخاص بك
git push -u origin main
