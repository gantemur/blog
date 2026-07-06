---
layout: "layouts/post.njk"
title: "Фаньяногийн давхар нумын томъёо"
date: "2019-01-04T06:31:23"
slug: "fagnano-doubling-formula"
permalink: "/2019/01/04/fagnano-doubling-formula/"
wordpress_id: 3022
wordpress_url: "https://t8m8r.wordpress.com/2019/01/04/fagnano-doubling-formula/"
categories: ["Анализ"]
tags: ["Жюлио Фаньяно", "давхар нумын томъёо", "давхар өнцгийн томъёо", "лемнискат", "эллипслэг интеграл"]
status: "publish"
comments_count: 0
math: true
generated_by: "wordpress-importer"
templateEngineOverride: "md"
---

Тойргийн интегралын зарим шинж чанарыг эллипслэг интеграл руу өргөтгөж болдог. Жишээ болгоод

\\(\displaystyle \theta=\arcsin x=\int_0^{x}\frac{dt}{\sqrt{1-t^2}}\\)

гэсэн тойргийн интегралыг авч үзье. Давхар өнцгийн синусын томъёог

\\(\sin2\theta=2\sin\theta\cos\theta=2\sin\theta\sqrt{1-\sin^2\theta}=2x\sqrt{1-x^2}\\)

маягтай бичээд

\\(2\arcsin x=\arcsin(2x\sqrt{1-x^2})\\)

гэсэн томъёог арксинусын хувьд гаргаж болно. Үүнийг интеграл хэлбэрээр бичвэл

\\(\displaystyle2\int_0^{x}\frac{dt}{\sqrt{1-t^2}}=\int\displaylimits_0^{2x\sqrt{1-x^2}}\frac{dt}{\sqrt{1-t^2}}.\qquad(*)\\)

Дээрх процессыг урвуулаад, давхар өнцгийн томъёог өөрийг нь тойргийн интеграл дээрх орлуулга мэтээр бас гаргаж болно. Тодруулбал, давхар өнцгийн томъёог гаргаж авахын тулд

\\(\displaystyle 2\int\frac{dx}{\sqrt{1-x^2}}=\int \frac{dy}{\sqrt{1-y^2}}\\)

чанарыг хангадаг \\(y=y(x)\\) эсвэл \\(x=x(y)\\) гэсэн орлуулга байх уу гэсэн асуултнаас эхэлж болно гэсэн үг. Хялбарыг бодоод \\((*)\\) томъёоноос будаа идвэл

\\(y=2x\sqrt{1-x^2}\\)

орлуулга ажиллах ёстой. Энэ дагуу зохих тооцоог хийвэл

\\(\displaystyle dy=\frac{2(1-2x^2)dx}{\sqrt{1-x^2}},\qquad 1-y^2=(1-2x^2)^2\\)

болох тул үнэхээр

\\(\displaystyle \frac{dy}{\sqrt{1-y^2}}=\frac{2(1-2x^2)dx}{(1-2x^2)\sqrt{1-x^2}}=\frac{2dx}{\sqrt{1-x^2}}\\)

гарна.

Эллипслэг интегралын хувьд \\((*)\\) хэлбэрийн анхны томъёог олсон хүн бол Италийн математикч [Жюлио Фаньяно](https://en.wikipedia.org/wiki/Giulio_Carlo_de%27_Toschi_di_Fagnano) юм. Тэр [Бернуллийн лемнискат](https://en.wikipedia.org/wiki/Lemniscate_of_Bernoulli) гэгдэх муруйг судлах явцдаа

\\(\displaystyle \int\frac{dx}{\sqrt{1-x^4}}\qquad(**)\\)

хэлбэрийн эллипслэг интегралтай тулгарсан байна. Энэ муруйн тэгшигэл нь туйлын координатад

\\(r^2=\cos2\theta\\)

бөгөөд

\\(rdr=-\sin2\theta d\theta,\qquad r^4+\sin^22\theta=\cos^22\theta+\sin^22\theta=1\\)

тул

\\(\displaystyle dr^2+r^2d\theta^2=dr^2+\frac{r^4dr^2}{\sin^22\theta}=\frac{dr^2}{1-r^4}\\)

буюу, \\(r=0\\) цэгээс \\(r=a\\) хүртэл явах нумын урт

\\(\displaystyle L(a)=\int_0^a\frac{dr}{\sqrt{1-r^4}}\\)

интегралаар өгөгдөнө.

[![](/blog/assets/wp-media/2019/01/lemniscate-2-e1546818020620.png)](https://t8m8r.wordpress.com/wp-content/uploads/2019/01/lemniscate-2.png) Бернуллийн лемнискат

Фаньяногийн 1715 оны үед олсон хувиргалт нь дараах 2 алхмаас тогтоно. Эхний орлуулга

\\(\displaystyle x=\frac{\sqrt2w}{\sqrt{1+w^4}},\qquad dx=\frac{\sqrt2(1-w^4)dw}{(\!\sqrt{1+w^4}\,)^3}\\)

бөгөөд, үр дүн нь

\\(\displaystyle \frac{dx}{\sqrt{1-x^4}}=\frac{\sqrt2dw}{\sqrt{1+w^4}}.\\)

Дараагийн орлуулга

\\(\displaystyle w=\frac{\sqrt2y}{\sqrt{1-y^4}},\qquad dw=\frac{\sqrt2(1+y^4)dy}{(\!\sqrt{1-y^4}\,)^3}\\)

бөгөөд, үр дүн нь

\\(\displaystyle \frac{dx}{\sqrt{1-x^4}}=\frac{\sqrt2dw}{\sqrt{1+w^4}}=\frac{2dy}{\sqrt{1-y^4}}.\\)

Хоёр орлуулгаа хамтатгаснаар

\\(\displaystyle x=\frac{\sqrt2w}{\sqrt{1+w^4}}=\frac{2y\sqrt{1-y^4}}{1+y^4}\\)

хувиргалт гарах ба, үүний үйлчлэл дор

\\(\displaystyle \int\frac{dx}{\sqrt{1-x^4}}=2\int \frac{dy}{\sqrt{1-y^4}}\\)

байна. Өөрөөр хэлбэл

\\(\displaystyle 2L(a)=L\Big(\frac{2a\sqrt{1-a^4}}{1+a^4}\,\Big)\\)

гэж бичиж болно. Лемнискатын нумын урт \\(L(a)\\)-г элементар функцүүдээр илэрхийлэх боломжгүй (үүнийг [Жозеф Лиувилль](https://en.wikipedia.org/wiki/Joseph_Liouville) 1833 онд баталсан) боловч, \\(L(a)\\) функцийг 2 дахин ихэсгэхэд шаардагдах аргументын утга \\(\frac{2a\sqrt{1-a^4}}{1+a^4}\\) гэсэн хялбар илэрхийллээр өгөгдөж байгаа нь маш сонирхолтой зүй тогтол юм.

[![](/blog/assets/wp-media/2019/01/Locandina-Fagnani-finalissima.jpg)](/blog/assets/wp-media/2019/01/Locandina-Fagnani-finalissima.jpg) Жюлио Фаньяно (1682–1766)
