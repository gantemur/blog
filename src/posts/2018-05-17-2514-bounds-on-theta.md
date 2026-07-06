---
layout: "layouts/post.njk"
title: "Чебышёвын θ функцийн үнэлгээ"
date: "2018-05-17T14:11:07"
slug: "bounds-on-theta"
permalink: "/2018/05/17/bounds-on-theta/"
wordpress_id: 2514
wordpress_url: "https://t8m8r.wordpress.com/2018/05/17/bounds-on-theta/"
categories: ["Тооны онол"]
tags: ["Чебышёв", "анхны тоо", "тета функц"]
status: "publish"
comments_count: 0
math: true
generated_by: "wordpress-importer"
templateEngineOverride: "md"
---

[Өмнөх постоороо](/blog/2018/05/17/bounds-on-psi/) бид дараах тэнцэл бишийг баталсан

\\(\displaystyle Ax-\frac52\ln x-1<\psi(x)<\frac65Ax+\frac5{4\ln6}\ln^2\!x+\frac54\ln x.\qquad\qquad(*)\\)

Үүнд \\(A=\ln\frac{2^{1/2}3^{1/3}5^{1/5}}{30^{1/30}}=0.9212\ldots\\) ба

\\(\displaystyle\psi(x)=\sum_{p^m\leq x}\ln p.\\)

Одоо энэ үнэлгээг

\\(\displaystyle\theta(x)=\sum_{p\leq x}\ln p\\)

функц рүү хөрвүүлэхийг оролдъё. Эдгээр функцүүдийн хооронд

\\(\displaystyle \psi(x)=\theta(x)+\theta\big(\!\sqrt{x}\,\big)+\theta\big(\!\sqrt[3]{x}\,\big)+\theta\big(\!\sqrt[4]{x}\,\big)+\ldots\\)

гэсэн холбоо байгаа. Үүний аргументийг \\(\sqrt{x}\\) болгож

\\(\displaystyle \psi\big(\!\sqrt{x}\,\big)=\theta\big(\!\sqrt{x}\,\big)+\theta\big(\!\sqrt[4]{x}\,\big)+\theta\big(\!\sqrt[6]{x}\,\big)+\ldots\\)

гэж нэг бичээд, анхны томъёоноос хасвал

\\(\displaystyle \psi(x)-\psi\big(\!\sqrt{x}\,\big)=\theta(x)+\theta\big(\!\sqrt[3]{x}\,\big)+\theta\big(\!\sqrt[5]{x}\,\big)+\ldots\\)

болох ба \\(\theta(x)\\) нь үл буурах монотон функц гэдгийг санавал

\\(\displaystyle \theta(x)\leq\psi(x)-\psi\big(\!\sqrt{x}\,\big)\qquad\qquad(\dagger)\\)

гэж шууд мөрдөнө. Нөгөө талаас, дээрхтэй төстэйгөөр

\\(\displaystyle \psi(x)-2\psi\big(\!\sqrt{x}\,\big)=\theta(x)-\theta\big(\!\sqrt{x}\,\big)+\theta\big(\!\sqrt[3]{x}\,\big)-\theta\big(\!\sqrt[4]{x}\,\big)+\theta\big(\!\sqrt[5]{x}\,\big)-\ldots\\)

гэж бичээд, мөн л \\(\theta(x)\\) функцийн монотон  чанарыг ашиглан дараах маягаар нөгөө талаас нь зааглаж болно.

\\(\displaystyle \theta(x)\geq\psi(x)-2\psi\big(\!\sqrt{x}\,\big)\qquad\qquad(\dagger\dagger)\\)

Одоо \\((*)\\) тэнцэл бишээ \\(\theta(x)\\) рүү хөрвүүлэхэд амархан. Үүний тулд

\\(\displaystyle A\sqrt{x}-\frac54\ln x-1<\psi\big(\!\sqrt{x}\,\big)<\frac65A\sqrt{x}+\frac5{16\ln6}\ln^2\!x+\frac58\ln x\\)

гэж бичээд, \\((\dagger)\\) ба \\((\dagger\dagger)\\) томъёонууддаа орлуулан дараах хоёр заагийг гаргаж авна.

\\(\theta(x)<\displaystyle\frac65Ax-A\sqrt{x}+\frac5{4\ln6}\ln^2\!x+\frac52\ln x+1\\)

\\(\theta(x)>\displaystyle Ax-\frac{12}5A\sqrt{x}-\frac5{8\ln6}\ln^2\!x-\frac{15}4\ln x-1\\)

Дорх зурагт эдгээр заагуудыг дүрсэлж үзүүлэв.

[![](/blog/assets/wp-media/2018/05/thest2.png)](/blog/assets/wp-media/2018/05/thest2.png) \\(Ax-\frac{12}5A\sqrt{x}-O(\ln^2\!x)<\theta(x)<\frac65Ax-A\sqrt{x}+O(\ln^2\!x)\\)

Энэ үнэлгээнийхээ хялбар хэрэглээ болгон, Чебышёв дараах асуултуудад бүрэн хариулт өгсөн.

 	
- Бид анхны тоонуудын урвуунуудын нийлбэр сарнидгийг мэднэ. Тэгвэл жишээ нь, \\(\displaystyle\sum_p\frac1{p\ln p}\\) гэсэн нийлбэр сарних уу?

 	
- Анхны тоонуудын тархалтын тухайд, жишээ нь \\(\frac12x<\pi(x)\ln x<\frac32x\\) гэсэн тэнцэл биш (\\(x\\) нь их үед) хүчинтэй юу?

 	
- Бертран таамаглал яг үнэн үү?

Эдгээр үр дүнг бид дараа дараачийн постуудаараа дэлгэрэнгүй авч үзнэ.
