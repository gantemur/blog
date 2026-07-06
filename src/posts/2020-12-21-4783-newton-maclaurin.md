---
layout: "layouts/post.njk"
title: "Ньютон-Маклорены тэнцэл бишүүд"
date: "2020-12-21T04:53:28"
slug: "newton-maclaurin"
permalink: "/2020/12/21/newton-maclaurin/"
wordpress_id: 4783
wordpress_url: "https://t8m8r.wordpress.com/2020/12/21/newton-maclaurin/"
categories: ["Анализ", "Тэнцэл биш"]
tags: ["Кошийн тэнцэл биш", "Маклорен", "Маклорены тэнцэл биш", "Ньютон", "Ньютоны тэнцэл биш"]
status: "publish"
comments_count: 0
math: true
generated_by: "wordpress-importer"
templateEngineOverride: "md"
---

Гурван эерэг тооны хувьд [Кошийн тэнцэл бишийг](/blog/2020/12/03/amgm/) санацгаая: 

\(\displaystyle  \sqrt[3]{abc} \leq \frac{a+b+c}3.\)

 Үүн дээр квадратлаг болон илүү ерөнхий [зэрэгт дунджуудыг](/blog/2020/12/04/power-mean/) нэмснээр 

\(\displaystyle  \sqrt[3]{abc} \leq \Big(\frac{\sqrt{a}+\sqrt{b}+\sqrt{c}}3\Big)^2 \leq\frac{a+b+c}3 \leq \sqrt{\frac{a^2+b^2+c^2}3}\)

 гэх мэт тэнцэл бишүүдийг бичиж болдог.

Сонирхолтой нь, Кошийн тэнцэл бишийг арай өөр чиглэлд бас сайжруулж болдгийг Кошигоос 100-аад жилийн өмнө Шотландын математикч [Колин Маклорен](https://en.wikipedia.org/wiki/Colin_Maclaurin) нээж, 1729 онд [хэвлүүлж](https://royalsocietypublishing.org/doi/10.1098/rstl.1729.0011) байжээ. Маклорены тэнцэл бишийг 3 эерэг тооны хувьд бичвэл 

\(\displaystyle  \sqrt[3]{abc} \leq \sqrt{\frac{ab+bc+ca}3}\leq\frac{a+b+c}3\)

 болно. Энэ тэнцэл биш нь Кошийн тэнцэл бишийг агуулах тул Кошийн тэнцэл бишийг Маклорен нээсэн гэж маргах ч боломжтой.

Цаашилбал, Маклорены тэнцэл бишүүд нь Ньютоны «[Универсаль арифметик](https://books.google.com/books?id=3_s2AAAAMAAJ)» номондоо 1707 онд баталгаагүйгээр хэвлүүлсэн 

\(\displaystyle  \frac{a+b+c}3\cdot abc \leq \Big(\frac{ab+bc+ca}3\Big)^2\)

 хэлбэрийн тэнцэл бишүүдээс мөрдөж гардаг. Ньютоны тэнцэл бишийг батлах гэж оролдож байгаад Маклорен өөрийнхөө тэнцэл бишийг нээсэн хэрэг.

Ньютон-Маклорены тэнцэл бишүүдийг ерөнхий тохиолдолд томъёолохын тулд хэд хэдэн тэмдэглэгээ оруулах хэрэгтэй. Юуны түрүүнд \({x_1,\ldots,x_n}\) гэсэн \({n}\) хувьсагчаас хамаарсан, \({k}\) зэргийн *элементар тэгшхэмт олон гишүүнтийг* [

\(\displaystyle  e_k=e_k(x_1,\ldots,x_n) = \sum_{1\leq i_1
] гэж тодорхойлдог. Жишээлбэл, \({n=3}\) үед 

\(\displaystyle  e_0=1,\quad e_1=x_1+x_2+x_3,\quad e_2=x_1x_2+x_1x_3+x_2x_3,\quad e_3=x_1x_2x_3.\)

 Ерөнхий тохиолдолд, эхний хоёр нь 

\(\displaystyle  e_0=1,\qquad e_1=x_1+\ldots+x_n,\)

 ба дараагийнх нь 

\(\displaystyle  e_2 = x_1x_2+x_1x_3+\ldots+x_1x_n+x_2x_3+\ldots+x_{n-1}x_n,\)

 бол, хамгийн сүүлийн хоёр нь 

\(\displaystyle  e_{n-1}=x_2\cdots x_n+x_1x_3\cdots x_n+\ldots+x_1\cdots x_{n-1}, \qquad e_n=x_1\cdots x_n,\)

 болно. Эндээс \({e_k}\) олон гишүүнт нь 

\(\displaystyle  \binom{n}{k} = \frac{n!}{k!(n-k)!}\)

 ширхэг гишүүнтэй болохыг ажиглаад, *тэгшхэмт дундаж* гэгчийг [

\(\displaystyle  E_k = \frac{e_k}{\binom{n}{k}} = \frac{k!(n-k)!}{n!} \sum_{1\leq i_1
] гэж тодорхойлдог. Ингээд бид Ньютон-Маклорены тэнцэл бишүүдийг томъёолоход бэлэн боллоо.

**Теорем 1 (Ньютон 1707).**  Дурын эерэг \({x_1,\ldots,x_n}\) тоонууд ба бүхэл \({1\leq k\leq n-1}\) тооны хувьд 

\(\displaystyle  E_{k-1}E_{k+1} \leq E_k^2, \qquad k=1,\ldots,n-1 \ \ \ \ \ (3)\)

 тэнцэл биш биелэх бөгөөд, тэнцэлдээ хүрэх нөхцөл нь \({x_1=\ldots=x_n}\). 

**Теорем 2 (Маклорен 1729).**  Дурын эерэг \({x_1,\ldots,x_n}\) тоонуудын хувьд 

\(\displaystyle  \sqrt[n]{E_n} \leq \sqrt[n-1]{E_{n-1}} \leq \ldots \leq \sqrt{E_2} \leq E_1 \ \ \ \ \ (4)\)

 тэнцэл биш биелэх ба, аль нэг нь тэнцэлдээ хүрсэн нөхцөлд \({x_1=\ldots=x_n}\). 

Маклорены тэнцэл бишийн эхний ба сүүлийн гишүүд \({\sqrt[n]{E_n} \leq E_1}\) гээд Кошийн тэнцэл бишийг өгч байгааг ажиглаарай. 

##  Маклорены тэнцэл бишийн баталгаа 

Маклорены тэнцэл бишийг Ньютоны тэнцэл бишийн мөрдлөгөө мэтээр баталъя. Юуны түрүүнд, \({E_0=1}\) гэдгийг тооцсоноор Ньютоны тэнцэл бишийн 

\(\displaystyle  E_0E_2\leq E_1^2\)

 тохиолдол нь 

\(\displaystyle  \sqrt{E_2}\leq E_1\)

 гэж өгнө. Одоо \({k\leq n-1}\) үед \({\sqrt[k]{E_k}\leq\sqrt[k-1]{E_{k-1}}}\) буюу 

\(\displaystyle  E_k^{k-1}\leq E_{k-1}^k\)

 гэж үзье. Ингээд Ньютоны тэнцэл бишийн \({E_{k-1}E_{k+1}\leq E_k^2}\) илэрхийллийг \({k}\) зэрэгт дэвшүүлээд, өмнөх нөхцлийг тооцвол 

\(\displaystyle  E_k^{k-1}E_{k+1}^k\leq E_{k-1}^kE_{k+1}^k\leq E_k^{2k} \qquad\Longrightarrow\qquad E_{k+1}^{k}\leq E_{k}^{k+1}\)

 гарч, Маклорены тэнцэл биш батлагдана.

Хэрэв \({E_{k+1}^{k}=E_{k}^{k+1}}\) бол, дээрх \({E_k^{k-1}E_{k+1}^k\leq E_{k-1}^kE_{k+1}^k\leq E_k^{2k}}\) тэнцэл бишээс 

\(\displaystyle  E_{k-1}^kE_{k+1}^k=E_k^{2k}\)

 гэж мөрдөх ба, Ньютоны тэнцэл бишийн тэнцэлдээ хүрэх нөхцөл нь \({x_1=\ldots=x_n}\) гэж өгнө.

##  Ньютоны тэнцэл бишийн баталгаа 

Энд бид хувьсагчийн тоо \({n}\)-ээр индукц хийнэ. Индукцийн суурь тохиолдол нь \({n=2}\) буюу \({E_0E_2\leq E_1^2}\) бөгөөд энэ нь Кошийн тэнцэл биш: 

\(\displaystyle  x_1x_2 \leq \Big( \frac{x_1+x_2}2 \Big)^2 .\)

 Одоо Ньютоны тэнцэл бишийг \({x_1,\ldots,x_{n-1}}\) гэсэн дурын \({n-1}\) эерэг тооны хувьд үнэн гэж үзээд, харгалзах олон гишүүнтүүдийг нь 

\(\displaystyle  \bar e_k = e_k(x_1,\ldots,x_{n-1}) , \qquad \bar E_k = \frac{\bar e_k}{\binom{n-1}{k}}\)

 гэж тэмдэглэе. Тэгвэл 

\(\displaystyle  e_k = \bar e_k + \bar e_{k-1}x_n = \binom{n-1}{k}\bar E_k + \binom{n-1}{k-1}\bar E_{k-1} x_n\)

 тул [

\(\displaystyle  E_k = \frac{e_k}{\binom{n}{k}} = \frac{n-k}n\bar E_k + \frac{k}n\bar E_{k-1} x_n \ \ \ \ \ (5)\)

] болно. Энд 

\(\displaystyle  \frac{\binom{n-1}{k}}{\binom{n}{k}} = \frac{(n-1)!}{k!(n-1-k)!}\cdot\frac{k!(n-k)!}{n!} = \frac{n-k}{n},\)

 болон 

\(\displaystyle  \frac{\binom{n-1}{k-1}}{\binom{n}{k}} = \frac{(n-1)!}{(k-1)!(n-k)!}\cdot\frac{k!(n-k)!}{n!} = \frac{k}{n},\)

 гэдгийг тооцсон. Мөн \({\bar E_n=0}\) гэвэл [(5)](#epf-newton-1) томъёо нь \({k=n}\) үед ч хүчинтэй. Бидний зорилго бол \({1\leq k\leq n-1}\) үед [

\(\displaystyle  E_{k-1}E_{k+1} \leq E_k \ \ \ \ \ (6)\)

] гэж харуулах явдал. Хэрэв 

\(\displaystyle  E_{k-1} = \frac{n-k+1}n\bar E_{k-1} + \frac{k-1}n\bar E_{k-2} x_n,\)

 ба 

\(\displaystyle  E_{k+1} = \frac{n-k-1}n\bar E_{k+1} + \frac{k+1}n\bar E_{k} x_n,\)

 илэрхийллүүдийг хооронд нь үржүүлбэл  

\(\displaystyle  E_{k-1}E_{k+1} = \frac{(n-k)^2-1}{n^2}\bar E_{k-1} \bar E_{k+1} + \frac{k^2-1}{n^2}x_n^2 \bar E_{k-2} \bar E_k \\ {}\qquad\qquad\qquad+ \frac{(n-k+1)(k+1)}{n^2}x_n \bar E_{k-1} \bar E_k + \frac{(n-k-1)(k-1)}{n^2}x_n \bar E_{k-2} \bar E_{k+1}\)

 гарна. Баруун гар талынх нь эхний 2 гишүүнийг \({n-1}\) хувьсагчтай Ньютоны тэнцэл бишийг ашиглан [

\(\displaystyle  \bar E_{k-1} \bar E_{k+1} \leq \bar E_{k}^2, \qquad \bar E_{k-2} \bar E_k \leq \bar E_{k-1}^2, \ \ \ \ \ (7)\)

] маягаар зааглаж болно. Эдгээрийг хооронд нь үржүүлбэл 

\(\displaystyle  \bar E_{k-2} \bar E_k \bar E_{k-1} \bar E_{k+1} \leq \bar E_{k-1}^2 \bar E_k^2\)

 болох ба үүнийг \({\bar E_{k-1}\bar E_k}\) үржвэрт хуваавал 

\(\displaystyle  \bar E_{k-2} \bar E_{k+1} \leq \bar E_{k-1}\bar E_k\)

 болж, дээрх \({E_{k-1}E_{k+1}}\) илэрхийллийн сүүлийн гишүүнийг 3 дахь гишүүнтэй нь төстэй илэрхийллээр зааглах боломж өгнө. Энэ бүгдийг дүгнэж бичвэл 

\(\displaystyle  E_{k-1}E_{k+1} \leq \frac{(n-k)^2-1}{n^2}\bar E_{k}^2 + \frac{k^2-1}{n^2}x_n^2 \bar E_{k-1}^2 + \frac{2k(n-k)+2}{n^2}x_n \bar E_{k-1} \bar E_k.\)

 Нөгөө талаас, [(5)](#epf-newton-1) иэлрхийллийг шууд квадрат зэрэгт дэвшүүлэн 

\(\displaystyle  E_{k}^2 = \frac{(n-k)^2}{n^2}\bar E_{k}^2 + \frac{k^2}{n^2}x_n^2 \bar E_{k-1}^2 + \frac{2k(n-k)}{n^2}x_n \bar E_{k-1} \bar E_k\)

 гэж олоод, үүнээсээ дээрх тэнцэл бишийг хассанаар 

\(\displaystyle  n^2(E_{k}^2-E_{k-1}E_{k+1}) \geq \bar E_{k}^2 + x_n^2 \bar E_{k-1}^2 - 2x_n \bar E_{k-1} \bar E_k = (\bar E_{k}-x_n \bar E_{k-1})^2\geq0\)

 гарч, Ньютоны тэнцэл биш батлагдана.

Хэрэв \({x_1,\ldots,x_{n-1}}\) тоонууд бүгд хоорондоо тэнцүү биш бол дээр ашиглагдсан [(7)](#epf-newton-2) тэнцэл бишүүд индукцийн нөхцөл ёсоор эрс байх тул эцсийн [(6)](#epf-newton-2a) тэнцэл биш мөн эрс байна. Харин \({x_1=\ldots=x_{n-1}=x}\) ба \({x_n\neq x}\) бол \({\bar E_{k-1}=x^{k-1}}\) ба \({\bar E_{k}=x^{k}}\) гэдгийг тооцон 

\(\displaystyle  \bar E_{k}-x_n \bar E_{k-1}=x^{k-1}(x-x_n)\neq0\)

 болж, эцсийн тэнцэл биш мөн эрс болоход хүрнэ. Теоремын баталгаа гүйцлээ.

##  Жишээнүүд 

**Жишээ 3.**  Эерэг \({a,b,c}\) тоонуудын хувьд 

\(\displaystyle  \sqrt[3]{abc} \leq \sqrt{\frac{ab+bc+ca}3}\leq\frac{a+b+c}3\)

 тэнцэл бишийг батал. 

*Бодолт.*  Энэ мэдээж Маклорины тэнцэл бишийн \({n=3}\) тохиолдол. Үүнийг шууд баталж үзье. Юуны өмнө 

\(\displaystyle  \sqrt[3]{ab\cdot bc\cdot ca} \leq \frac{ab+bc+ca}3\)

 гэдгээс эхний тэнцэл биш нь гарна. Дараа нь 

\(\displaystyle  (a+b+c)^2 = \frac{a^2+b^2}2+\frac{b^2+c^2}2+\frac{c^2+a^2}2 + 2ab+2bc+2ca\)

 гэж бичээд, 

\(\displaystyle  \frac{a^2+b^2}2+\frac{b^2+c^2}2+\frac{c^2+a^2}2\geq ab+bc+ca\)

 заагийг санавал хоёрдахь тэнцэл биш нь батлагдана. \(\Box\)

**Жишээ 4.**  Эерэг \({a,b,c}\) тоонууд \({ab+bc+ca=3}\) нөхцлийг хангадаг бол 

\(\displaystyle  a^3+b^3+c^3+6abc\geq9\)

 гэж харуул. 

*Бодолт.*  [Шурын тэнцэл бишээс](/blog/2020/12/17/schur-inequality/) 

\(\displaystyle  \begin{array}{rcl}  a^3+b^3+c^3+6abc &\geq& a^2(b+c)+b^2(c+a)+c^2(a+b) + 3abc\\ &=& a(ab+ac+bc)+b(bc+ba+ac)+c(ca+cb+ab) \\ &=& 3(a+b+c) \end{array}\)

 гэж гарах ба одоо Маклорены тэнцэл бишийг ашиглавал 

\(\displaystyle  \frac{a+b+c}3\geq\sqrt{\frac{ab+bc+ca}3}=1\)

 болж, бодлого бодогдоно. \(\Box\)

 [![](/blog/assets/wp-media/2020/12/newtonmaclaurin.jpg)](/blog/assets/wp-media/2020/12/newtonmaclaurin.jpg) Исаак Ньютон (1643–1727). Колин Маклорин (1698–1746).
