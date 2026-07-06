---
layout: "layouts/post.njk"
title: "Бернуллийн тэнцэл биш"
date: "2020-12-18T21:59:09"
slug: "bernoulli-inequality-2"
permalink: "/2020/12/18/bernoulli-inequality-2/"
wordpress_id: 4769
wordpress_url: "https://t8m8r.wordpress.com/2020/12/18/bernoulli-inequality-2/"
categories: ["Анализ", "Тэнцэл биш"]
tags: ["Бернулли", "Бернуллийн тэнцэл биш", "Кошийн тэнцэл биш", "Эйлерийн тоо", "Юнгийн тэнцэл биш"]
status: "publish"
comments_count: 0
math: true
generated_by: "wordpress-importer"
templateEngineOverride: "md"
---

[Бернуллийн тэнцэл биш](https://en.wikipedia.org/wiki/Bernoulli%27s_inequality) гэдгээр бид \({\alpha>1}\) эсэхээс хамаараад \({(1+x)^\alpha\geq 1+\alpha x}\) эсвэл \({(1+x)^\alpha\leq 1+\alpha x}\) хэлбэрийн тэнцэл бишийг ойлгодог. Энэ алдарт тэнцэл бишийг [Якоб Бернулли](https://en.wikipedia.org/wiki/Jacob_Bernoulli) 1689 онд [хэвлүүлсэн номондоо](https://archive.org/stream/jacobibernoulli00conggoog#page/n494) оруулснаас үүдэн Бернуллигээр овоглох болсон. Гэвч үнэндээ Бернуллийг 13 настай байхад Бельгийн математикч  [Рене-Франсуа де Слюз](https://en.wikipedia.org/wiki/René-François_de_Sluse) энэ тэнцэл бишийг [хэвлүүлж байжээ](https://books.google.com/books?id=ugJ1GtyH08kC&pg=PA114).

**Теорем 1.**  Хэрэв \({x\geq-1}\) нь бодит тоо, \({0

\(\displaystyle  (1+x)^q\leq1+qx, \ \ \ \ \ (1)\)

] тэнцэл биш биелэх ба, тэнцэлдээ хүрэх нөхцөл нь \({x=0}\). Харин \({y\geq-1}\) нь бодит тоо, \({p>1}\) нь рациональ тоо бол [

\(\displaystyle  1+py\leq(1+y)^p , \ \ \ \ \ (2)\)

] тэнцэл биш биелэх ба, тэнцэлдээ хүрэх нөхцөл нь \({y=0}\). 

 

##  Баталгаа 

[Жинтэй Кошийн тэнцэл бишийн](/blog/2020/12/03/amgm/) хоёр хувьсагчтай үеийн тухайн тохиолдлыг санацгаая.

**Теорем 2.**  Сөрөг биш \({a,b}\) тоонууд, \({0\leq\lambda\leq1}\) рациональ тооны хувьд [

\(\displaystyle  a^{\lambda}b^{1-\lambda}\leq \lambda a+(1-\lambda)b , \ \ \ \ \ (3)\)

] тэнцэл биш биелэх ба, тэнцэлдээ хүрэх нөхцөл нь \({a=b}\). 

Эндээс шууд [

\(\displaystyle  (1+x)^{q}=(1+x)^{q}\cdot1^{1-q} \leq q(1+x) + (1-q)\cdot1 = 1+qx , \ \ \ \ \ (4)\)

] маягаар эхний [(1)](#eBernoulli-sub) тэнцэл биш мөрдөнө. Үүндээ \({y=qx}\) ба \({p=1/q}\) гэсэн орлуулга хийвэл 

\(\displaystyle  (1+py)^{1/p} \leq 1+y ,\)

 буюу 

\(\displaystyle  1+py \leq (1+y)^p ,\)

 тэнцэл биш \({y\geq-1/p}\) үед хүчинтэй нь харагдана. Тэнцэлдээ хүрэх нөхцөл нь \({y=0}\) байх нь ч тодорхой. Цаашилбал, \({-1\leq y<-1/p}\) үед 

\(\displaystyle  1+py<0\leq(1+y)^p ,\)

 тул Бернуллийн тэнцэл биш бүрэн батлагдлаа.

**Тэмдэглэл 3.**  Энэ баталгааны гарааны цэг болсон [(4)](#ebenroulli-pf-start) тэнцэл бишийг [Юнгийн тэнцэл биш](/blog/2020/12/17/young-inequality/) дээр үндэслэн гаргаж ч болох байсан: 

\(\displaystyle  (1+x)^q\cdot 1\leq \frac{[(1+x)^q]^{1/q}}{1/q} + \frac{1^{1/(1-q)}}{1/(1-q)} = 1 +qx.\)

 Өөрөөр хэлбэл Бернуллийн тэнцэл биш нь Кошийн болон Юнгийн тэнцэл бишийн аль алиных нь мөрдлөгөө болно. Дараагийн хэсэгт бид Кошийн тэнцэл биш нь өөрөө Бернуллийн тэнцэл бишийн мөрдлөгөө гэж харуулна. 

**Тэмдэглэл 4.**  Логарифм функцийн өсөх чанар ашигласан нэгэн баталгааг [эндээс](/blog/2018/12/24/bernoulli-inequality/) үзэж болно. 

##  Кошийн тэнцэл биш 

Бернуллийн тэнцэл бишээс [Кошийн тэнцэл бишийг](/blog/2020/12/03/amgm/) гаргаж болдог. Үүнд \({a_1,a_2,\ldots}\) гэсэн эерэг тоонууд аваад, 

\(\displaystyle  A_n = \frac{a_1+\ldots+a_n}n\)

 гэж бичье. Тэгвэл 

\(\displaystyle  A_n^n = \Big( \frac{(n-1)A_{n-1}+a_n}{n} \Big)^n = A_{n-1}^n \Big( 1 + \frac1n\big(\frac{a_n}{A_{n-1}} - 1\big) \Big)^n\)

 болох ба, Бернуллийн тэнцэл бишээс 

\(\displaystyle  A_n^n \geq A_{n-1}^n \Big( 1 + \big(\frac{a_n}{A_{n-1}} - 1\big) \Big) = a_nA_{n-1}^{n-1}\)

 гэж гарна. Энэ 

\(\displaystyle  A_n^n \geq a_nA_{n-1}^{n-1}\)

 тэнцэл биш Кошийн тэнцэл бишээс «арай хүчтэй». Учир нь үүнийг давтан хэрэглэснээр Кошийн тэнцэл биш батлагдана: 

\(\displaystyle  A_n^n \geq a_nA_{n-1}^{n-1} \geq a_na_{n-1}A_{n-2}^{n-2} \geq\ldots\geq a_na_{n-1}\ldots a_1 .\)

##  Жишээнүүд 

**Жишээ 5.**  Дурын натурал \({n\geq2}\) тооны хувьд 

\(\displaystyle  \sqrt{\frac21} + \sqrt[3]{\frac32} + \ldots + \sqrt[n]{\frac{n}{n-1}} \leq \frac{n^2-1}n\)

 гэж харуул. 

*Бодолт.*  Бернуллийн тэнцэл бишээс 

\(\displaystyle  \sqrt[n]{\frac{n}{n-1}} = \sqrt[n]{1+\frac{1}{n-1}} \leq 1 + \frac{1}{n(n-1)} = 1 + \frac1{n-1}-\frac1n\)

 гарах ба үүнийг шууд нийлбэрчилснээр бидний батлах гэсэн тэнцэл биш мөрдөнө. \(\Box\)

**Жишээ 6.**  Рационал \({0\(\displaystyle  a^b+b^a>1\)

 гэж харуул. 

*Бодолт.*  Бернуллийн тэнцэл бишээс 

\(\displaystyle  \big(\frac1a\big)^b=\big(1+\frac1a-1\big)^b\leq1+b\big(\frac1a-1\big) = \frac{a+b-ab}a < \frac{a+b}a\)

 ба 

\(\displaystyle  \big(\frac1b\big)^a< \frac{b+a}b\)

 тул 

\(\displaystyle  a^b+b^a>\frac{a}{a+b}+\frac{b}{b+1}=1\)

 болно. \(\Box\)

**Жишээ 7.**  Дурын натурал \({n}\)-ийн хувьд 

\(\displaystyle  \Big(1+\frac1n\Big)^{n} < \Big(1+\frac1{n+1}\Big)^{n+1}\)

 гэж батал. 

*Бодолт.*  Дорх томъёонуудыг хялбарчлах үүднээс \({n}\)-ийн оронд \({n-1}\) гэж бичье. Ингээд 

\(\displaystyle  \Big(1+\frac1{n-1}\Big)^{n-1} = \Big(\frac{n}{n-1}\Big)^{n-1} = \Big(1-\frac1n\Big)^{1-n}\)

 гэдгийг ажиглаад, Бернуллийн тэнцэл бишийг хэрэглэн 

\(\displaystyle  \frac{(1+\frac1{n})^n}{(1+\frac1{n-1})^{n-1}} = \frac{(1+\frac1{n})^n}{(1-\frac1n)^{1-n}} = \frac{(1-\frac1{n^2})^n}{1-\frac1n} > \frac{1-\frac{n}{n^2}}{1-\frac1n} = 1\)

 гэж харснаар баталгаа дуусна. \(\Box\)

**Жишээ 8.**  Дурын натурал \({n}\)-ийн хувьд 

\(\displaystyle  \Big(1+\frac1n\Big)^{n+1} > \Big(1+\frac1{n-1}\Big)^{n}\)

 гэж харуул. 

*Бодолт.*  Бернуллийн тэнцэл бишээс 

\(\displaystyle  \frac{(1+\frac1{n-1})^n}{(1+\frac1{n})^n} = \Big( 1+\frac1{n^2-1} \Big)^n >1+\frac{n}{n^2-1}\)

 гэдгийг ажиглаад, 

\(\displaystyle  \frac{(1+\frac1{n-1})^n}{(1+\frac1{n})^{n+1}} = \frac{(1+\frac1{n-1})^n}{(1+\frac1{n})^{n}(1+\frac1{n})} > \frac{1+\frac{n}{n^2-1}}{1+\frac1{n}} > 1\)

 гэсэн харьцааг сонирхсноор бодлого бодогдоно. \(\Box\)

**Жишээ 9.**  Дурын эерэг \({a}\) ба натурал \({n}\)-ийн хувьд 

\(\displaystyle  \frac{1-\frac1a}{n} \leq \sqrt[n]{a} - 1 \leq \frac{a-1}n\)

 гэж батал (Тухайлбал эндээс шууд \({n\rightarrow\infty}\) үед \({\sqrt[n]{a}\rightarrow1}\) гэж гарна). 

*Бодолт.*  Хэрэв \({x=a-1>-1}\) гэвэл Бернуллийн тэнцэл бишээс 

\(\displaystyle  \sqrt[n]{a} = (1+x)^{1/n} \leq 1+ \frac{x}n\)

 тул, дээд зааг нь батлагдана. Одоо \({y=1-\frac1a<1}\) гэвэл 

\(\displaystyle  \frac1{\sqrt[n]{a}} = \big(\frac1a\big)^{\frac1n}=(1-y)^{1/n} \leq 1-\frac{y}n\)

 буюу 

\(\displaystyle  \sqrt[n]{a} \geq \frac1{1-\frac{y}n}\)

 болох ба, эндээс 

\(\displaystyle  \sqrt[n]{a} - 1 \geq \frac{y/n}{1-\frac{y}n} \geq \frac{y}n\)

 гэж гарна. \(\Box\)

**Жишээ 10.**  Дурын натурал \({n}\)-ийн хувьд 

\(\displaystyle  \sqrt[n]{n}< \Big( 1 + \frac1{\sqrt{n}} \Big)^2\)

 гэж харуул (Тухайлбал эндээс шууд \({n\rightarrow\infty}\) үед \({\sqrt[n]{n}\rightarrow1}\) гэж гарна). 

*Бодолт.*  Юуны түрүүнд 

\(\displaystyle  \sqrt[n]{n} = n^{1/n} = \big( \sqrt{n} \big)^{2/n} \leq \big( 1+\sqrt{n} \big)^{2/n}\)

 гэдгийг ажиглаад, Бернуллийн тэнцэл бишийг хэрэглэн 

\(\displaystyle  \Big( 1+\frac1{\sqrt{n}} \Big)^n >1+\frac{n}{\sqrt{n}} = 1 + {\sqrt{n}}\)

 гэж харснаар баталгаа дуусна. \(\Box\)

 [![](/blog/assets/wp-media/2020/12/sleuzebernoulli.jpg)](/blog/assets/wp-media/2020/12/sleuzebernoulli.jpg) Рене-Франсуа де Слюз (1622–1685). Якоб Бернулли (1655–1705).
