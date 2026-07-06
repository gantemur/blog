---
layout: "layouts/post.njk"
title: "Абелийн тэнцэл биш"
date: "2020-12-28T23:11:30"
slug: "abel-inequality"
permalink: "/2020/12/28/abel-inequality/"
wordpress_id: 4840
wordpress_url: "https://t8m8r.wordpress.com/2020/12/28/abel-inequality/"
categories: ["Анализ", "Тэнцэл биш"]
tags: ["Абелийн нийлбэрийн томъёо", "Абелийн тэнцэл биш", "Абель", "Сайжруулсан Чебышёв"]
status: "publish"
comments_count: 0
math: true
generated_by: "wordpress-importer"
templateEngineOverride: "md"
---

Норвегийн суут математикч [Нильс Хенрик Абель](https://en.wikipedia.org/wiki/Niels_Henrik_Abel) 26 наслахдаа математикт хичнээн шинэ зүйл сэдэж, хичнээн шинэ салбарын үрийг тарьсан нь гайхалтай. Түүний хүрсэн бусад амжилтуудтай харьцуулахад хэт энгийн мэт боловч маш өргөн ашиглагддаг нэг үр дүн байдаг нь түүний нэрээр нэрлэгдсэн нийлбэрийн томъёо билээ. Бид одоо энэ нийлбэрийн томъёотой нягт уялдаатай, орчин үеийн математикт нэвчсэн нэг том урсгалын эхлэл дээр байдаг нэгэн тэнцэл бишийг авч үзэх гэж байна.

Хэрэв \({\{a_k\}}\) ба \({\{b_k\}}\) нь тоон дарааллууд бол  

\(\displaystyle  \sum_{k=1}^na_k(c_{k+1}-c_k) =\sum_{k=1}^na_kc_{k+1}-a_1c_1-\sum_{k=1}^{n-1}a_{k+1}c_{k+1}\\ {}\qquad\qquad=a_nc_{n+1}-a_1c_1-\sum_{k=1}^{n-1}(a_{k+1}-a_k)c_{k+1}\)

  байна. Үүнийг [Абелийн хэсэгчилсэн нийлбэрийн томъёо](/blog/2018/05/20/abel-summation/) гэдэг.

Одоо \({\{c_k\}}\) гэсэн нэг шинэ дараалал аваад, \({b_1=0}\) ба 

\(\displaystyle  b_k = c_1+\ldots+c_{k-1},\)

 гэвэл Абелийн томъёо ёсоор  

\(\displaystyle  \sum_{k=1}^n a_kc_k =\sum_{k=1}^n a_k(b_{k+1}-b_k) =a_nb_{n+1}-a_1b_1-\sum_{k=1}^{n-1}(a_{k+1}-a_k)b_{k+1}\\ {}\qquad\qquad=a_nb_{n+1}+\sum_{k=1}^{n-1}(a_k-a_{k+1})b_{k+1}\)

  гарна. Энд \({a_1\geq a_2\geq\ldots\geq a_1\geq0}\) ба \({M=\max _ib_i}\) гэж үзвэл 

\(\displaystyle  \sum_{k=1}^n a_kc_k \leq Ma_n+M\sum_{k=1}^{n-1}(a_k-a_{k+1}) =Ma_1\)

 болж, *Абелийн тэнцэл биш* гэгддэг дараах үр дүн мөрдөнө.

**Теорем 1.**  Үл өсөх, эерэг \({a_1,\ldots,a_n}\) дараалал ба дурын \({c_1,\ldots,c_n}\) дарааллын хувьд [

\(\displaystyle  m a_1 \leq a_1c_1+\ldots+a_nc_n \leq M a_1 \ \ \ \ \ (1)\)

] тэнцэл биш биелнэ. Үүнд 

\(\displaystyle  m= \min\{c_1,c_1+c_2,\ldots,c_1+\ldots+c_n\} ,\)

 ба 

\(\displaystyle  M = \max\{c_1,c_1+c_2,\ldots,c_1+\ldots+c_n\} .\)

 

##  Жишээнүүд 

Абелийн тэнцэл биш болон Абелийн томъёог ашигласан хэдэн жишээ авч үзве.

**Жишээ 2.**  Хэрэв \({a_1,\ldots,a_n}\) ба \({0\(\displaystyle  a_1^2\leq b_1^2,\quad a_1^2+a_2^2\leq b_1^2+b_2^2,\qquad \ldots,\qquad a_1^2+\cdots+a_n^2\leq b_1^2+\cdots+b_n^2\)

 нөхцлийг хангадаг бол 

\(\displaystyle  \frac{a_1^2}{b_1}+\ldots+\frac{a_n^2}{b_n} \leq b_1+\ldots+b_n\)

 тэнцэл биш биелнэ гэж харуул. 

*Бодолт.*  Тэнцэл бишийнхээ баруун зүүн гар талын ялгаврыг 

\(\displaystyle  \Delta = \sum_i b_i-\sum_i\frac{a_i^2}{b_i} = \sum_i\frac1{b_i}\cdot\big( b_i^2-a_i^2 \big)\)

 гэж бичээд, Абелийн тэнцэл бишийг хэрэглэвэл 

\(\displaystyle  \Delta \geq \frac1{b_1}\cdot \min\big\{ b_1^2-a_1^2, b_1^2 - a_1^2 + b_2^2 - a_2^2, b_1^2 - a_1^2 +\cdots+b_n^2 - a_n^2 \big\} \geq0\)

 гарч, бодлого бодогдоно. \(\Box\)

**Жишээ 3.**  Хэрэв \({a_1,\ldots,a_n}\) ба \({b_1\geq b_2\geq\ldots\geq b_n}\) гэсэн эерэг тоон дарааллууд 

\(\displaystyle  a_1\geq b_1,\quad a_1a_2\geq b_1b_2,\qquad \ldots,\qquad a_1\cdots a_n\geq b_1\cdots b_n\)

 нөхцлийг хангадаг бол 

\(\displaystyle  a_1+\ldots+a_n\geq b_1+\ldots+b_n\)

 тэнцэл биш биелнэ гэж харуул. 

*Бодолт.*  Тэнцэл бишийнхээ зүүн баруун гар талын ялгаврыг 

\(\displaystyle  \sum_i a_i-\sum_ib_i = \sum_ib_i\big( \frac{a_i}{b_i} - 1 \big)\)

 гэж бичээд, Абелийн тэнцэл бишийг хэрэглэвэл 

\(\displaystyle  \sum_i a_i-\sum_ib_i \geq b_1 \cdot \min\big\{ \frac{a_1}{b_1} - 1, \frac{a_1}{b_1} + \frac{a_2}{b_2} - 2, \frac{a_1}{b_1} +\ldots+ \frac{a_n}{b_n} - n \big\}\)

 гарах ба Кошийн тэнцэл бишээс 

\(\displaystyle  \frac{a_1}{b_1} +\ldots+ \frac{a_m}{b_m} \geq m\sqrt[m]{\frac{a_1\cdots a_n}{b_1\cdots b_n}} \geq m\)

 гэдгийг тооцсоноор \({\sum_i a_i-\sum_ib_i\geq0}\) болж, бодлого бодогдоно. \(\Box\)

**Жишээ 4 (Сайжруулсан Чебышёв).**  Хэрэв \({\{a_k\}}\), \({\{b_k\}}\) дарааллууд 

\(\displaystyle  a_1\geq a_2,\quad a_1+a_2\geq2a_3, \qquad\ldots,\qquad a_1+\ldots+a_{n-1}\geq(n-1)a_n\)

 ба 

\(\displaystyle  b_1\geq b_2,\quad b_1+b_2\geq2b_3, \qquad\ldots,\qquad b_1+\ldots+b_{n-1}\geq(n-1)b_n\)

 нөхцлүүдийг хангадаг бол 

\(\displaystyle  n(a_1b_1+\ldots+a_nb_n)\geq(a_1+\ldots+a_n)(b_1+\ldots+b_n)\)

 гэж батал. 

*Бодолт.*  Юуны өмнө, \({c_0=0}\) ба 

\(\displaystyle  c_{k+1}=b_1+\ldots+b_k\)

 гээд, \({a_{n+1}=0}\) гэсэн тодорхойлолттойгоор Абелийн томъёог хэрэглэн 

\(\displaystyle  \sum_ka_kb_k =\sum_ka_k(c_{k+1}-c_k) = \sum_{k=1}^n (a_k-a_{k+1})c_{k+1} = \sum_{k=1}^n k(a_k-a_{k+1})\frac{c_{k+1}}{k}\)

 гэж бичье. Одоо \({d_0=0}\) ба 

\(\displaystyle  d_{k+1} =a_1-a_1+2(a_2-a_3)+\ldots+k(a_k-a_{k+1}) =a_1+a_2+\ldots+a_k-ka_{k+1}\)

 гээд, Абелийн томъёог дахин хэрэглэвэл 

\(\displaystyle  \sum_ka_kb_k = \sum_{k=1}^n \frac{c_{k+1}}{k} (d_{k+1}-d_{k}) = \frac{c_{n+1}d_{n+1}}{n} + \sum_{k=1}^{n-1} \big( \frac{c_{k+1}}{k} - \frac{c_{k+2}}{k+1} \big) d_{k+1}\)

 гарна. Эцэст нь, бодлогын 

\(\displaystyle  b_1+\ldots+b_{k}\geq kb_{k+1}\)

 нөхцлөөс 

\(\displaystyle  (k+1)b_1+\ldots+(k+1)b_{k}\geq kb_1+\ldots+kb_{k}+kb_{k+1}\)

 буюу 

\(\displaystyle  \frac{c_{k+1}}{k} \geq \frac{c_{k+2}}{k+1}\)

 гэж мөрдөх тул 

\(\displaystyle  \sum_ka_kb_k \geq \frac{c_{n+1}d_{n+1}}{n} = \frac{(b_1+\ldots+b_n)(a_1+\ldots+a_n)}n\)

 болж, бидний батлах гэсэн тэнцэл биш батлагдана. \(\Box\)

 [![](/blog/assets/wp-media/2020/12/1cqxc6gsvnycncgptpd8era.png)](/blog/assets/wp-media/2020/12/1cqxc6gsvnycncgptpd8era.png) Нильс Хенрик Абель (1802–1829).
