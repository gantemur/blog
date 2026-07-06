---
layout: "layouts/post.njk"
title: "Факториал функцийн үнэлгээ"
date: "2018-05-17T02:47:51"
slug: "bounds-on-factorials"
permalink: "/2018/05/17/bounds-on-factorials/"
wordpress_id: 2507
wordpress_url: "https://t8m8r.wordpress.com/2018/05/17/bounds-on-factorials/"
categories: ["Анализ", "Тооны онол"]
tags: ["Стирлингийн томъёо", "Трапецийн арга", "факториал"]
status: "publish"
comments_count: 0
math: true
generated_by: "wordpress-importer"
templateEngineOverride: "md"
---

[Өмнөх постоороо](/blog/2018/05/16/chebyshev-functions/) бид Чебышёвын

\\(\displaystyle \psi(x)=\sum_{p^m\leq x}\ln p\\)

функц нь бидний *үндсэн адилтгал* гэж нэрлэсэн

\\(\displaystyle {T(x)=\sum_{k\geq1}\psi\Big({\frac{x}k}\Big)}\\)

харьцаагаар

\\(\displaystyle T(x)=\ln[x]!=\sum_{n\leq x}\ln n\\)

функцтэй холбогддог болохыг баталсан. Энэ \\(T(x)\\) функц нь үнэндээ факториал функц учир Стирлингийн

\\(\displaystyle n!\sim\sqrt{2\pi n}\Big(\frac{n}e\Big)^n\\)

эсвэл

\\(\displaystyle \ln n!=n\ln n-n+\frac12\ln n+\ln\sqrt{2\pi}+O(n^{-1})\\)

томъёоны тусламжтайгаар ойролцоолж болох бөгөөд эндээсээ үндсэн адилтгалын тусламжтайгаар \\(\psi(x)\\) функцийн талаар мэдээлэл гарган авах нь бидний (буюу Чебышёвын) гол төлөвлөгөө байгаа.

Энэ постны зорилго бол Стирлингийн томъёоноос хамааралгүйгээр өөрсдөө хялбар аргаар \\(T(x)\\) функцийг хангалттай хүчтэй зааганд оруулахад оршино.

**Теорем.** Дурын \\(x\geq1\\) бодит тооны хувьд

\\(\displaystyle T(x)
ба

\\(\displaystyle T(x)>x\ln x-x-\frac12\ln x+\frac78\\)

тэнцэл бишүүд хүчинтэй. Эдгээр заагийг дорх зурагт дүрсэлж үзүүлэв.

[![](/blog/assets/wp-media/2018/05/factorial.png)](/blog/assets/wp-media/2018/05/factorial.png) \\(x\ln x-x-\frac12\ln x+\frac78 < T(x) < x\ln x-x+\frac12\ln x+1\\)

**Баталгаа.** Эхлээд \\(T(x)\\) функцийг дээрээс нь зааглахын тулд, \\(n=[x]\\) гээд, зурагт үзүүлснээр \\(f(x)=\ln x\\) функцийн \\([1,x]\\) завсар дээрх интегралыг \\(1,2,\ldots,n,x\\) абсцисстай босоо шулуунууд хэвтээ тэнхлэг ба \\(f\\) функцийн графиктай огтлолцоход үүсэх цэгүүдээр тодорхойлогдсон трапецуудын талбайгаар ойролцоолъё.

[![](/blog/assets/wp-media/2018/05/traplog.png)](/blog/assets/wp-media/2018/05/traplog.png)

Тодруулбал, \\(f\\) нь гүдгэр функц гэдгийг ашиглан

\\(\displaystyle\int_1^xf(x)dx>\frac{f(1)+f(2)}2+\frac{f(2)+f(3)}2+\ldots+\frac{f(n-1)+f(n)}2+\frac{f(n)+f(x)}2\\)

болохыг харахад амархан. Эндээс

\\(\displaystyle\sum_{k=1}^nf(k)<\int_1^xf(x)dx+\frac{f(1)+f(x)}2\\)

гэж гарах ба \\(f(x)=\ln x\\) орлуулга хийснээр

\\(\displaystyle T(x)=\sum_{k=1}^n \ln k<\int_1^x\ln x\,dx-\frac{\ln x}2=x\ln x-x+1+\frac{\ln x}2\\)

болж, дээд зааг батлагдана.

Одоо доод заагийг нь батлахын тулд, \\(f\\) функцийн графикийн \\(1,2,\ldots,n\\) абсцисстай цэгүүд дээр шүргэгч татаад, \\(\frac12,\frac32,\ldots,\\) абсцисстай босоо шулуунуудтай огтлолцуулах замаар трапецууд байгуулъя. Хэрэв \\(x-n>\frac12\\) бол энэ трапецууд \\(f\\) функцийн графикийг хараахан бүрхэж чадахгүй тул, \\([x-\frac12,x]\times[0,f(x)]\\) гэсэн тэгш өнцөгтийг бас нэмж өгье.

[![](/blog/assets/wp-media/2018/05/tanglog.png)](/blog/assets/wp-media/2018/05/tanglog.png)

Тэгвэл

\\(\displaystyle\int_1^xf(d)dx<\frac14\cdot\frac{f'(1)}2+\frac{f(1)}2+f(2)+f(3)+\ldots+f(n)+\frac{f(x)}2\\)

буюу

\\(\displaystyle \sum_{k=1}^nf(k)>\int_1^xf(x)dx+\frac{f(1)}2-\frac{f'(1)}8-\frac{f(x)}2\\)

гэсэн тэнцэл бишид хүрнэ. Ингээд \\(f(x)=\ln x\\) гэж орлуулан

\\(\displaystyle T(x)=\sum_{k=1}^n\ln k>\int_1^x\ln x\,dx-\frac18-\frac{\ln x}2=x\ln x-x+1-\frac18-\frac{\ln x}2\\)

болж, доод зааг батлагдана.

**Дасгал.** Дараах тэнцэл бишийг эерэг бүхэл \\(n\\) болгоны хувьд батал.

\\(\displaystyle \ln n!>n\ln n-n+\frac{\ln n}2+\frac78+\frac1{8n}\\)
