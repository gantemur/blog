---
layout: "layouts/post.njk"
title: "Урвуу анхны тоонуудын нийлбэр"
date: "2018-05-04T22:04:23"
slug: "prime-reciprocal-sum"
permalink: "/2018/05/04/prime-reciprocal-sum/"
wordpress_id: 124
wordpress_url: "https://t8m8r.wordpress.com/2018/05/04/prime-reciprocal-sum/"
categories: ["Тооны онол"]
tags: ["Эйлер", "анхны тоо", "гармоник цуваа"]
status: "publish"
comments_count: 0
math: true
generated_by: "wordpress-importer"
templateEngineOverride: "md"
---

Евклидийн теоремийн [Эйлерийн баталгаанд](http://t8m8r.wordpress.com/2010/04/26/euclid-thm-euler-pf/) дараах адилтгал шийдвэрлэх үүрэг гүйцэтгэсэн

\(\displaystyle\prod_{i=1}^{n}\frac{1}{1-\frac1{p_i}}=\sum_{m\in M(n)}\frac1{m}\qquad\qquad\qquad(*).\)

Үүнд \(M(n)\) нь анхны тоон задаргаандаа  \(p_n\)-ээс их анхны тоог агуулдаггүй тоонуудын олонлог

\(M(n)=\{p_1^{k_1}p_2^{k_2}\ldots p_n^{k_n}:k_i\geq0\}.\)

Жишээ нь \(M(1)\) нь 2-ын сөрөг биш зэргүүдээс тогтсон олонлог, \(M(2)\) нь 2 ба 3-ын сөрөг биш зэргүүдийн үржвэрүүдээс тогтсон олонлог гэх мэт. Арифметикийн үндсэн теоремаас тухайлбал үргэлж

\(1,2,\ldots,n\in M(n)\)

байх тул \(n\to\infty\) үед \(M(n)\) олонлог натурал тоон олонлогийг бүрхэх нь ойлгомжтой. Тэгэхээр (1) адилтгалын баруун гар тал дахь нийлбэр \(n\to\infty\) үед (гармоник цуваа учир) сарних ба ингэснээр уг адилтгалын зүүн гар тал дахь үржвэр мөн сарнихад хүрч төгсгөлгүй олон анхны тоо оршин байх нь батлагдана. Бид яг энэ аргументаараа \(x\)-ээс хэтрэхгүй анхны тоонуудын тоо

\(\pi(x)+1\geq\ln x\)

тэнцэтгэл бишийг хангана гэдгийг бас баталсан. Үүнд \(\ln x\) нь натурал (*e* суурьтай) логарифмыг тэмдэглэнэ.

Анхны тоонуудын нягтыг үнэлэх өөр нэг арга бол

\(\displaystyle\sum_{i=1}^\infty\frac1{p_i}=\frac12+\frac13+\frac15+\frac17+\frac1{11}+\ldots\)

цуваа сарних эсэхийг шалгах явдал юм. Гармоник цуваа

\(\displaystyle\sum_{i=1}^\infty\frac1{i}=1+\frac12+\frac13+\frac14+\ldots=\infty\)

сарнидаг боловч дурын эерэг \({}\varepsilon>0\) параметрийн хувьд

\(\displaystyle\sum_{i=1}^\infty\frac1{i^{1+\varepsilon}}=1+\frac1{2^{1+\varepsilon}}+\frac1{3^{1+\varepsilon}}+\ldots<\infty\)

цуваа нийлдэг болохыг бид мэднэ. Тэгэхээр хэрэв \(\sum_{i=1}^\infty\frac1{p_i}\) цуваа сарнидаг бол \(1,2^{1+\varepsilon},3^{1+\varepsilon},4^{1+\varepsilon},\ldots\) дарааллыг бодвол анхны тоонуудын дараалал илүү шигүү тархалттай байдаг гэсэн үг.

Дээрх цувааны сарнилтыг шалгахын тулд (*) тэнцэтгэлийн хоёр талаас логарифм авъя:

\(\displaystyle-\sum_{i=1}^{n}\ln\Big(1-\frac1{p_i}\Big)=\ln\left(\sum_{m\in M(n)}\frac1{m}\right).\)

Үүний баруун гар талыг

\(\displaystyle\ln\left(\sum_{m\in M(n)}\frac1{m}\right)\geq\ln\left(1+\frac12+\ldots+\frac1n\right)\geq\ln\ln(n+1)\)

гэж үнэлж болно. Харин зүүн гар талыг нь, ямар ч \(0\leq x\leq\frac12\) тооны хувьд хүчинтэй

\(\displaystyle\ln(1-x)+2x\geq0\qquad\qquad(**)\)

тэнцэл бишийг (дорх зургийг үз) ашиглан

\(\displaystyle-\sum_{i=1}^{n}\ln\Big(1-\frac1{p_i}\Big)\leq\sum_{i=1}^{n}\frac2{p_i}\)

гэж бичиж болно. Эдгээр үр дүнг нэгтгэвэл

\(\displaystyle2\sum_{i=1}^{n}\frac1{p_i}\geq\ln\ln(n+1)\)

болох тул анхны тоонуудын урвуунуудын нийлбэр хязгааргүй гарах нь мөрдөнө.

Дээрх баталгааны суурь нь Эйлерийн (*) адилтгал байсан. Энэ адилтгал нь [Эйлерийн үржвэр](/blog/2010/08/18/euler-prod/) гэгддэг

\(\displaystyle\zeta(s)=\sum_{n}\frac1{n^s}=\prod_p\frac1{1-p^{-s}}\)

тэнцэтгэлд хүргэдэг бөгөөд Евклидийн теорем нь \(s\to1\) үед \(\zeta(s)\to\infty\) гэдгээс шууд гардаг. Одоо анхны тоонуудын урвуунуудын нийлбэрийг энэ өнцгөөсөө харах гэж оролдъё. Эйлерийн үржвэрээс логарифм аваад, (**) тэнцэл бишийг ашиглавал

\(\displaystyle\ln\zeta(s)=-\sum_p\ln(1-p^{-s})\leq2\sum_p\frac1{p^s}\)

болох ба \(s\to1\) үед \(\ln\zeta(s)\to\infty\) тул \(\sum\frac1p\) цуваа сарних нь ерөнхийдөө харагдана. Энэ санааг дараах маягаар найдвартай болгож болно. Эхлээд \(s>1\) үед

\(\displaystyle \sum_{p}\frac1{p^s}<\sum_{n}\frac1{n^s}<\infty\)

гэдгээс \(m\to\infty\) хязгаарт

\(\displaystyle f(m,s)=\sum_{p>m}\frac1{p^s}\to0\)

гэдгийг харна. Хичнээн ч том \(N\) тоо өгөгдсөн байсан гэсэн, \(s>1\) тоог 1-д ойрхон сонгох замаар

\(\displaystyle\sum_p\frac1{p^s}>\frac12\zeta(s)>N\)

болгох боломжтой. Одоо \(m\) тоог \(f(m,s)<1\) байхаар сонговол

\(\displaystyle N<\sum_p\frac1{p^s}=\sum_{p\leq m}\frac1{p^s}+f(m,s)<\sum_{p\leq m}\frac1p+1\)

болж, бидний батлах гэсэн үр дүн гарч ирнэ.

[![](/blog/assets/wp-media/2018/05/log1.png)](/blog/assets/wp-media/2018/05/log1.png) \(f(x)=\ln(1-x)+2x\) функцийн график

**Даалгавар:** Ямар ч \(0\leq x\leq\frac12\) бодит тооны хувьд \(\displaystyle\ln(1-x)+2x\geq0\) тэнцэтгэл биш биелнэ гэж батал.
