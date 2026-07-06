---
layout: "layouts/post.njk"
title: "Сонины нийлбэрийн томъёо"
date: "2018-05-21T16:07:22"
slug: "sonin-summation"
permalink: "/2018/05/21/sonin-summation/"
wordpress_id: 2635
wordpress_url: "https://t8m8r.wordpress.com/2018/05/21/sonin-summation/"
categories: ["Анализ", "Тооны онол"]
tags: ["Сонины нийлбэр", "Стирлинг", "Эйлер-Маскероний тогтмол", "Эйлерийн нийлбэр"]
status: "publish"
comments_count: 0
math: true
generated_by: "wordpress-importer"
templateEngineOverride: "md"
---

[Өмнөх постоор](/blog/2018/05/20/abel-summation/) бид Абелийн нийлбэрийн томъёо гэгддэг дараах томъёог баталсан:

\\(\displaystyle\sum_{k\leq x}f(k)\gamma_k=f(x)g(x)-\int_{1}^xg(t)f'(t)dt\\)

Үүнд \\(\gamma_1,\gamma_2,\ldots\\) нь тоон дараалал, \\(f(x)\\) нь тасралтгүй дифференциалчлагддаг функц ба

\\(g(x)=\displaystyle\sum_{k\leq x}\gamma_k.\\)

Хэрэв \\(\gamma_k=1\\) гэвэл \\(g(x)=[x]\\) болох тул

\\(\displaystyle\sum_{k\leq x}f(k)=[x]f(x)-\int_{1}^x[t]f'(t)dt=[x]f(x)-\int_{1}^xtf'(t)dt+\int_{1}^x\{t\}f'(t)dt\\)

Үүндээ

\\(\displaystyle\int_{1}^xtf'(t)dt=xf(x)-f(1)-\int_{1}^xf(t)dt\\)

гэдгийг орлуулбал

\\(\displaystyle\sum_{k\leq x}f(k)=-\{x\}f(x)+f(1)+\int_{1}^xf(t)dt+\int_{1}^x\{t\}f'(t)dt\\)

болно. Ингээд сүүлийн интеграл дотор \\(-\frac12\\) гэсэн гишүүн нэмснээр

\\(\displaystyle\sum_{k\leq x}f(k)=\Big({\frac12}-\{x\}\Big)f(x)+\frac{f(1)}2+\int_{1}^xf(t)dt+\int_{1}^x\Big(\{t\}-{\frac12}\Big)f'(t)dt\\)

гэсэн томъёо гарч ирнэ. Үүнийг [Николай Яковлевич Сонины](https://en.wikipedia.org/wiki/Nikolay_Yakovlevich_Sonin) нэрээр *Сонины томъёо*, эсвэл *Эйлерийн томъёо* гэх нь бий.

**Шууд баталгаа.** Сонины томъёог хэсэгчилсэн интеграл ашиглан шууд батлая. Юуны түрүүнд

\\(\displaystyle\int_{k}^{k+1}f(t)dt=\int_{k}^{k+1}f(t)d(t-k-{\textstyle\frac12})\\{}\qquad=\big(t-k-{\textstyle\frac12}\big)f(t)\Big|_k^{k+1}-\int_{k}^{k+1}\big(t-k-{\textstyle\frac12}\big)f'(t)dt\\{}\qquad=\frac{f(k)+f(k+1)}2-\int_{k}^{k+1}\big(\{t\}-{\textstyle\frac12}\big)f'(t)dt\\)

томъёог \\(k=1,\ldots,n-1\\) индексүүдээр нийлбэрчилбэл

\\(\displaystyle\int_{1}^{n}f(t)dt=\sum_{k=1}^{n-1}\int_{k}^{k+1}f(t)dt\\{}\qquad=\frac{f(1)}2+f(2)+\ldots+f(n-1)+\frac{f(n)}2-\int_{1}^{n}\big(\{t\}-{\textstyle\frac12}\big)f'(t)dt\\)

буюу

\\(\displaystyle\sum_{k=1}^nf(k)=\frac{f(1)+f(n)}2+\int_{1}^{n}f(t)dt+\int_{1}^{n}\big(\{t\}-{\textstyle\frac12}\big)f'(t)dt\\)

гарна. Одоо \\(n=[x]\\) гэж аваад,

\\(\displaystyle\int_{n}^{x}\big(\{t\}-{\textstyle\frac12}\big)f'(t)dt=\int_{n}^{x}\big(t-n-{\textstyle\frac12}\big)f'(t)dt=\big(t-n-{\textstyle\frac12}\big)f(t)\Big|_n^x-\int_{n}^{x}f(t)dt\\{}\qquad=\big(\{x\}-{\textstyle\frac12}\big)f(x)+\frac{f(n)}2-\int_{n}^{x}f(t)dt\\)

гэдгийг тооцон, баталгаа дуусна.

**Жишээ.** Сонины томъёог \\(f(n)=\frac1n\\) үед хэрэглэвэл

\\(\displaystyle\sum_{n\leq x}\frac1n=\ln x+\frac{\frac12-\{x\}}x+\frac12-\int_{1}^x\frac{\{t\}-\frac12}{t^2}dt\\)

гарна. Одоо \\(|\{t\}-\frac12|\leq\frac12\\) гэдгээс сүүлийн интеграл \\(x\to\infty\\) хязгаарт абсолют нийлэх тул

\\(\displaystyle\sum_{n\leq x}\frac1n=\ln x+\underbrace{\frac12-\int_{1}^\infty\frac{\{t\}-\frac12}{t^2}dt}_{\gamma}+\underbrace{\frac{\frac12-\{x\}}x+\int_{x}^\infty\frac{\{t\}-\frac12}{t^2}dt}_{\varepsilon(x)}\\)

гэж бичиж болно гэсэн үг. Энд \\(x\to\infty\\) хязгаарт \\(\varepsilon(x)\to0\\) ба

\\(\displaystyle\gamma=\frac12-\int_{1}^\infty\big(\{t\}-{\textstyle\frac12}\big)\frac{dt}{t^2}=0.5772156649\ldots\\)

нь *Эйлер-Маскероний тогтмол*. Өөрөөр хэлбэл

\\(\displaystyle\gamma=\lim_{n\to\infty}\Big(1+\frac12+\ldots+\frac1n-\ln n\Big)\\)

хязгаар оршин байна.

[![](/blog/assets/wp-media/2018/05/eulergamma1.png)](/blog/assets/wp-media/2018/05/eulergamma1.png) \\(1+\frac12+\ldots+\frac1n-\ln n\\)

Энэ жишээг жаахан өргөтгөе.

**Лемм.** Хэрэв \\(f:(0,\infty)\to\mathbb{R}\\) нь тасралтгүй дифференциалчлагддаг,  уламжлал нь монотон бөгөөд \\(x\to\infty\\) хязгаарт \\(f'(x)\to0\\) байдаг функц бол дараах томъёо хүчинтэй.

\\(\displaystyle\sum_{k\leq x}f(k)=\gamma(f)+\int_{1}^xf(t)dt+\big({\textstyle\frac12}-\{x\}\big)f(x)+\varepsilon(x).\\)

Үүнд

\\(\displaystyle\gamma(f)=\frac{f(1)}2+\int_{1}^\infty\big(\{t\}-{\textstyle\frac12}\big)f'(t)dt\\)

интеграл нийлэх ба

\\(\displaystyle\varepsilon(x)=-\int_{x}^\infty\big(\{t\}-{\textstyle\frac12}\big)f'(t)dt\\)

**Баталгаа.** Юуны түрүүнд интегралын дундаж утгын тухай теорем ёсоор, \\(1\\(\displaystyle\int_{a}^b\big(\{t\}-{\textstyle\frac12}\big)f'(t)dt=f'(a)\int_{a}^x\big(\{t\}-{\textstyle\frac12}\big)dt+f'(b)\int_{x}^b\big(\{t\}-{\textstyle\frac12}\big)dt\\)

байх \\(x\in(a,b)\\) цэг олдоно. Баруун гар тал дахь интегралууд нь зааглагдсан тул дээрх интеграл \\(a,b\to\infty\\) үед 0 рүү тэмүүлнэ. Иймд Кошийн шинжүүрээр \\(\gamma(f)\\) тогтмолыг тодорхойлж байгаа интеграл нийлнэ.

**Жишээ.** Дээрх леммд \\(f(x)=\ln x\\) гэж орлуулбал

\\(\displaystyle\sum_{k\leq x}\ln k=\gamma(\ln)+x\ln x-x+\big({\textstyle\frac12}-\{x\}\big)\ln x+\varepsilon(x).\\)

Үүнд

\\(\displaystyle\gamma(\ln)=\int_{1}^\infty\big(\{t\}-{\textstyle\frac12}\big)\frac{dt}t,\qquad \varepsilon(x)=-\int_{x}^\infty\big(\{t\}-{\textstyle\frac12}\big)\frac{dt}t.\\)

Хэрэв \\(x=n\\) нь бүхэл гэвэл бидний «Стирлингийн ойролцоолол» гэж ярьдаг томъёо гарч ирнэ:

\\(\displaystyle\ln n!=\gamma(\ln)+n\ln n-n+{\textstyle\frac12}\ln n+\varepsilon(n)\\)

буюу \\(C=e^{\gamma(\ln)}\\) орлуулгатайгаар

\\(\displaystyle n!\sim Cn^ne^{-n}\sqrt{n}.\\)

Энэ томъёог 1733 онд [Абрахам де Муавр](https://en.wikipedia.org/wiki/Abraham_de_Moivre) нээсэн ба [Жеймс Стирлингийн](https://en.wikipedia.org/wiki/James_Stirling_(mathematician)) оруулсан хувь нэмэр нь \\(C=\sqrt{2\pi}\\) гэдгийг тодорхойлсон явдал болно.

[![](/blog/assets/wp-media/2018/05/stirlingconstant.png)](/blog/assets/wp-media/2018/05/stirlingconstant.png) \\(f(n)=\ln(n!)+n-n\ln n-\frac12\ln n\\)

Стирлингийн томъёоны \\(\varepsilon(n)\\) гишүүнийг үнэлэхийг оролдъё. Нэг талаас

\\(\displaystyle\int_k^{k+1}\big(\{t\}-{\textstyle\frac12}\big)\frac{dt}t=\int_k^{k+1}(t-k-{\textstyle\frac12})\frac{dt}t=\frac{t-k-{\frac12}}{2t}\Big|_k^{k+1}+\int_k^{k+1}\frac{(t-k-{\frac12})^2}{t^2}{dt}\\{}\qquad=\frac1{8(k+1)}-\frac1{8k}+\int_k^{k+1}\frac{(\{t\}-{\frac12})^2}{t^2}{dt}\\)

тул

\\(\displaystyle\varepsilon(n)=-\int_{n}^\infty\big(\{t\}-{\textstyle\frac12}\big)\frac{dt}t=\frac1{8n}-\int_n^{\infty}\frac{(\{t\}-{\frac12})^2}{t^2}{dt}<\frac1{8n}.\\)

Нөгөө талаас,

\\(\displaystyle\int_k^{k+1}\big(\{t\}-{\textstyle\frac12}\big)\frac{dt}t=\int_k^{k+1}\frac{t-k-{\frac12}}{t}{dt}=-\int_0^{\frac12}\frac{{\frac12}-t}{k+t}{dt}+\int_{\frac12}^1\frac{t-{\frac12}}{k+t}{dt}\\{}\qquad=-\int_0^{\frac12}\frac{sds}{k+{\frac12}-s}+\int_0^{\frac12}\frac{sds}{k+{\frac12}+s}=-\int_0^{\frac12}\frac{2s^2ds}{(k+{\frac12})^2-s^2}\\)

тул

\\(\displaystyle\varepsilon(n)=-\int_{n}^\infty\big(\{t\}-{\textstyle\frac12}\big)\frac{dt}t=\sum_{k=n}^\infty\int_0^{\frac12}\frac{2s^2ds}{(k+{\frac12})^2-s^2}>0.\\)

Эцэст нь дүгнэхэд

\\(\displaystyle {}n\ln n-n+\frac{\ln n+\ln2\pi}2<\ln n!
