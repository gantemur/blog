---
layout: "layouts/post.njk"
title: "Абелийн нийлбэрийн томъёонууд"
date: "2018-05-20T19:30:22"
slug: "abel-summation"
permalink: "/2018/05/20/abel-summation/"
wordpress_id: 2633
wordpress_url: "https://t8m8r.wordpress.com/2018/05/20/abel-summation/"
categories: ["Анализ", "Тооны онол"]
tags: ["Абель", "нийлбэр", "хэсэгчилсэн интеграл", "хэсэгчилсэн нийлбэр"]
status: "publish"
comments_count: 0
math: true
generated_by: "wordpress-importer"
templateEngineOverride: "md"
---

Энэ постоор бид [Нильс Хенрик Абелийн](https://en.wikipedia.org/wiki/Niels_Henrik_Abel) нээсэн, *Абелийн хэсэгчилсэн нийлбэрийн томъёо* гэгддэг, хоорондоо нягт уялдаатай хоёр томъёог батална.

**Теорем 1** (Абель 1826). \(\{a_k\}\) ба \(\{b_k\}\) гэсэн хоёр дараалал өгөгдсөн болог. Тэгвэл

\(\displaystyle\sum_{k=0}^na_k(b_{k+1}-b_k)=a_nb_{n+1}-a_0b_0-\sum_{k=0}^{n-1}(a_{k+1}-a_k)b_{k+1}.\)

Үүнийг дараах маягаар шууд баталж болно:

\(\displaystyle\sum_{k=0}^na_k(b_{k+1}-b_k)=\sum_{k=0}^na_kb_{k+1}-a_0b_0-\sum_{k=0}^{n-1}a_{k+1}b_{k+1}\\{}\qquad=a_nb_{n+1}-a_0b_0-\sum_{k=0}^{n-1}(a_{k+1}-a_k)b_{k+1}\)

Дээрх томъёо хэсэгчилсэн интегралын

\(\displaystyle\int_a^b f(t)g'(t)dt=f(b)g(b)-f(a)g(a)-\int_a^bg(t)f'(t)dt\)

томъёотой төстэй байгааг анзаараарай.

**Жишээ.** Бид \(-1\(\displaystyle\arctan x=x-\frac{x^3}3+\frac{x^5}5-\frac{x^7}7+\ldots\qquad(*)\)

цуваа нийлдэгийг мэднэ. Тэгвэл

\(\displaystyle\frac\pi4=1-\frac13+\frac15-\frac17+\ldots\)

томъёо биелэх үү гэсэн асуултыг сонирхоцгооё. Абелийн томъёог \(a_k=x^{2k+1}\) ба

\(\displaystyle b_0=0,\quad b_1=1,\quad b_2=1-\frac13,\quad b_3=1-\frac13+\frac15,\ldots\)

үед хэрэглэн (*) цувааны эхний \(n\) гишүүний нийлбэрийг

\(\displaystyle f_n(x)=\sum_{k=0}^na_k(b_{k+1}-b_k)=b_{n+1}x^{2n+1}-\sum_{k=0}^{n-1}b_{k+1}(x^2-1)x^{2k+1}\)

гэж бичиж болно. Одоо \(\{b_k\}\) нь нийлэх дараалал тул зааглагдсан гэдгийг тооцон, \(-1\(\displaystyle f(x)=\arctan x=(1-x^2)\sum_{k=0}^{\infty}b_{k+1}x^{2k+1}\)

гарах ба,

\(\displaystyle b=\lim_{k\to\infty} b_k=1-\frac13+\frac15-\frac17+\ldots\)

хязгаарыг хоёр талаас нь хасвал

\(\displaystyle f(x)-b=(1-x^2)\sum_{k=0}^{\infty}(b_{k+1}x-b)x^{2k}\qquad(**)\)

болно. Үүнд

\(\displaystyle 1=(1-x^2)\sum_{k=0}^{\infty}x^{2k}\)

гэдгийг ашигласан. Эндээс \(x\to1\) үед \(f(x)\to b\) гэж харуулахын тулд, \(\varepsilon>0\) гэсэн (өчүүхэн бага) тоо өгөгдсөн гэж үзээд, \(n\) болон \(\delta>0\) тоонуудыг, \(k>n\) ба \(1-\delta\(\displaystyle |b_{k+1}x-b|=|(b_{k+1}-b)x+b(x-1)|\leq|b_{k+1}-b|+|b|\cdot|x-1|\)

тэнцэл бишээс харж болно. Үүнийгээ (**) илэрхийлэлд орлуулбал

\(\displaystyle |f(x)-b|\leq(1-x^2)\sum_{k=0}^{n}|b_{k+1}x-b|x^{2k}+\varepsilon(1-x^2)\sum_{k=n+1}^{\infty}x^{2k}\\{}\qquad\leq(1-x^2)\sum_{k=0}^{n}|b_{k+1}x-b|x^{2k}+\varepsilon\to\varepsilon\)

болох тул, \(1-\rho0\) тоог сонгож авах боломжтой. Эцэст нь дүгнэхэд, \(x\to1\) үед нэг талаас \(f(x)\to b\), нөгөө талаас \(f(x)=\arctan x\to\frac\pi4\) тул \(b=\frac\pi4\) гэж мөрдөнө.

Абелийн хоёрдахь томъёо нь нийлбэр, интегралыг хольсон «эрлийз» томъёо болно.

**Теорем 2.** \(\gamma_1,\gamma_2,\ldots\) гэсэн тоон дараалал, мөн \(f(x)\) гэсэн тасралтгүй дифференциалчлагддаг функц бүрийн хувьд

\(\displaystyle\sum_{k\leq x}f(k)\gamma_k=f(x)g(x)-\int_{1}^xg(t)f'(t)dt\)

тэнцэтгэл биелнэ. Үүнд

\(g(x)=\displaystyle\sum_{k\leq x}\gamma_k.\)

**Баталгаа.** Эхлээд \(n=[x]\) гээд, \(\gamma_k=g(k)-g(k-1)\) гэдгийг ашиглан, хэсэгчилсэн нийлбэрийн томъёогоор

\(\displaystyle\sum_{k\leq x}f(k)\gamma_k=\sum_{k=0}^nf(k)\big(g(k)-g(k-1)\big)=f(n)g(n)-\sum_{k=0}^{n-1}g(k)\big(f(k+1)-f(k)\big)\)

болно. Сүүлийн гишүүнийг цааш нь

\(\displaystyle\sum_{k=0}^{n-1}g(k)\big(f(k+1)-f(k)\big)=\sum_{k=0}^{n-1}g(k)\int_k^{k+1}f'(t)dt=\sum_{k=0}^{n-1}\int_k^{k+1}g(t)f'(t)dt\\{}\qquad=\int_0^{n}g(t)f'(t)dt=\int_1^{n}g(t)f'(t)dt\)

гэж хувиргаснаар

\(\displaystyle\sum_{k\leq x}f(k)\gamma_k=f(n)g(n)-\int_1^{n}g(t)f'(t)dt\)

гарна. Ингээд

\(\displaystyle\int_n^{x}g(t)f'(t)dt=g(n)\int_n^{x}f'(t)dt=g(n)f(x)-g(n)f(n)=g(x)f(x)-g(n)f(n)\)

тул теорем батлагдлаа.

**Жишээ.** \(f(x)=\ln x,\,\,\gamma_k=1\) гэвэл \(g(x)=[x]\) болох ба Абелийн нийлбэрийн томъёогоор

\(\displaystyle\sum_{k\leq x}\ln k=[x]\ln x-\int_1^x\frac{[t]}tdt=[x]\ln x-\int_1^x\frac{t-\{t\}}tdt\\{}\qquad=x\ln x-\{x\}\ln x-(x-1)+\int_1^x\frac{\{t\}}tdt\\{}\qquad=x\ln x-\big(\{x\}-{\textstyle\frac12}\big)\ln x-(x-1)+\int_1^x\frac{\{t\}-\frac12}tdt\)

гарна. Үүнд \(\{x\}=x-[x]\) нь \(x\)-ийн бутархай хэсэг. Одоо \(|\{t\}-\frac12|\leq\frac12\) гэдгийг ашиглавал

\(\displaystyle x\ln x-x+1-\ln x\leq\sum_{k\leq x}\ln k\leq x\ln x-x+1+\ln x\)

болно.

Хэрэв \(x=n\) нь бүхэл бол, эхний томъёо маань шууд

\(\displaystyle \ln n!=n\ln n-n+1+\int_1^n\frac{\{t\}}tdt=n\ln n-n+\frac12\ln n+1+\int_1^n\frac{\{t\}-\frac12}tdt\)

болж хувирна.

Энд бид яагаад \(\{t\}-\frac12\) гэсэн функцийг интеграл дор оруулахыг чухалчлаад байна вэ гэвэл энэ функцийн дундаж нь 0 учраас интегралын утга бага байх магадлал их учраас тэр. Бид дараагийн постоороо энэ жишээг өргөтгөж, ерөнхий томъёо гаргаж авна.

[![](/blog/assets/wp-media/2018/05/frac.png)](/blog/assets/wp-media/2018/05/frac.png) ({x} – ½) / x функцийн график
