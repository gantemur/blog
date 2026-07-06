---
layout: "layouts/post.njk"
title: "Анхны тоон индекстэй цуваанууд"
date: "2018-05-18T16:37:45"
slug: "series-indexed-by-primes"
permalink: "/2018/05/18/series-indexed-by-primes/"
wordpress_id: 2525
wordpress_url: "https://t8m8r.wordpress.com/2018/05/18/series-indexed-by-primes/"
categories: ["Анализ", "Тооны онол"]
tags: ["Чебышёв", "анхны тоо", "цуваа"]
status: "publish"
comments_count: 0
math: true
generated_by: "wordpress-importer"
templateEngineOverride: "md"
---

Анхны тоонуудын урвуунуудын цуваа сарнидаг болохыг [Эйлер баталсан](/blog/2018/05/04/prime-reciprocal-sum/). Үүнийг гармоник цувааны сарнилтай харьцуулж бодож болно. Тэгвэл, жишээ нь

\\(\displaystyle\frac1{2\ln2}+\frac1{3\ln3}+\frac1{4\ln4}+\frac1{5\ln5}+\frac1{6\ln6}+\ldots\\)

цуваа сарнидагтай адилаар

\\(\displaystyle\frac1{2\ln2}+\frac1{3\ln3}+\frac1{5\ln5}+\frac1{7\ln7}+\frac1{11\ln11}+\ldots\\)

цуваа бас сарних уу гэсэн асуулт гарна. Иймэрхүү асуултуудад Чебышёв дараах теоремоороо бүрэн хариулт өгсөн.

**Теорем.** \\(t_2,t_3,t_4,\ldots\\) дараалал нь эерэг тоонуудаас бүтэх ба

\\(\displaystyle\frac{t_2}{\ln2}\geq\frac{t_3}{\ln3}\geq\frac{t_4}{\ln4}\geq\ldots\\)

чанарыг хангадаг болог. Тэгвэл

\\(\displaystyle\sum_pt_p=t_2+t_3+t_5+t_7+t_{11}+t_{13}+\ldots\\)

цувааны нийлэх эсэх нь 

\\(\displaystyle\sum_{n}\frac{t_n}{\ln n}=\frac{t_2}{\ln2}+\frac{t_3}{\ln3}+\frac{t_4}{\ln4}+\frac{t_5}{\ln5}+\frac{t_6}{\ln6}+\ldots\\)

цувааны нийлэх эсэхтэй эквивалент.

Теоремыг батлахын өмнө, үүнийг ашигласан хэдэн жишээ авч үзье. Юуны өмнө, Эйлерийн үр дүн

\\(\displaystyle\sum_n\frac1{n\ln n}=\infty\qquad\Longrightarrow\qquad\sum_p\frac1p=\infty\\)

гээд шууд гарна. Цаашилбал,

\\(\displaystyle\sum_n\frac1{n\ln^2\!n}<\infty\qquad\Longrightarrow\qquad\sum_p\frac1{p\ln p}<\infty\\)

байна. Тэгэхээр анхны тоон \\(\{p\}\\) дараалал нь \\(\{n\ln^2\!n\}\\) дарааллыг бодвол шигүү (ө.х. удаанаар өсдөг) боловч, \\(\{p\ln p\}\\) тоонууд нь \\(\{n\ln n\}\\) дарааллаас мэдэгдэхүйц хурднаар өсдөг гэсэн үг. Үнэндээ \\(\sum\frac1p\\) цувааны ерөнхий гишүүний хуваарьт логарифмын ямар ч эерэг зэрэг бичсэн гэсэн цуваа нийлнэ (Дасгал!). Нөгөө талаас, давхар логарифм бол бичиж болно:

\\(\displaystyle\sum_n\frac1{n\ln n\ln\ln n}=\infty\qquad\Longrightarrow\qquad\sum_p\frac1{p\ln\ln p}=\infty\\)

Энэ юу гэсэн үг вэ гэвэл \\(\{p\ln\ln p\}\\) дараалал нь \\(\{n\ln^2\!n\}\\) (түүнчлэн \\(\{n\ln n(\ln\ln n)^2\}\\)) дарааллыг бодвол удаан өснө гэсэн үг.

**Теоремын баталгаа.** Чебышёвын

\\(\displaystyle\theta(x)=\sum_{p\leq x}\ln p\\)

функц дээр

\\(F(x)<\theta(x)
гэсэн заагийг [бид баталсан](/blog/2018/05/17/bounds-on-theta/). Үүнд

\\(F(x)=\displaystyle Ax-\frac{12}5A\sqrt{x}-\frac5{8\ln6}\ln^2\!x-\frac{15}4\ln x-1\\)

\\(G(x)=\displaystyle\frac65Ax-A\sqrt{x}+\frac5{4\ln6}\ln^2\!x+\frac52\ln x+1\\)

бөгөөд \\(A=\ln\frac{2^{1/2}3^{1/3}5^{1/5}}{30^{1/30}}=0.9212\ldots\\) нь тогтмол тоо.

Хэрэв \\(k\\) нь анхны тоо бол \\(\theta(k)-\theta(k-1)=\ln k\\), харин зохиомол тоо бол \\(\theta(k)-\theta(k-1)=0\\) байх нь мэдээж. Тэгэхээр

\\(\displaystyle\sum_{p\leq n}t_p=\sum_{k\leq n}\frac{\theta(k)-\theta(k-1)}{\ln k}\,t_k\qquad\qquad(**)\\)

гэж бичиж болно. Энэ нийлбэрийн нэмэгдэхүүнүүдийг

\\(\begin{array}{rcl}\displaystyle\sum_{p\leq n}t_p&=&\displaystyle\frac{\theta(2)}{\ln2}\,t_2+\frac{\theta(3)-\theta(2)}{\ln3}\,t_3+\ldots+\frac{\theta(n)-\theta(n-1)}{\ln n}\,t_n\\&=&\displaystyle\Big(\frac{t_2}{\ln2}-\frac{t_3}{\ln3}\Big)\theta(2)+\ldots+\Big(\frac{t_{n-1}}{\ln(n-1)}-\frac{t_n}{\ln n}\Big)\theta(n-1)+\frac{t_n}{\ln n}{\theta(n)}\end{array}\\)

маягаар бүлэглээд, \\(\{{t_n}/{\ln n}\}\\) нь үл өсөх дараалал гэдгийг санавал, \\(\theta(\cdot)\\)-ийн өмнөх коэффициентууд дандаа сөрөг биш тоонууд болох нь харагдана. Иймд \\((*)\\) томъёон дахь дээд доод заагийг \\((**)\\) нийлбэрт орсон \\(\theta(\cdot)\\) болгоны хувьд шууд хэрэглэвэл, уг нийлбэрийн дээд доод зааг харгалзан гарч ирнэ:

\\(\displaystyle\frac{F(2)t_2}{\ln2}+\sum_{k=3}^n\big({F(k)-F(k-1)}\big)\frac{t_k}{\ln k}<\sum_{p\leq n}t_p<\frac{G(2)t_2}{\ln2}+\sum_{k=3}^n\big({G(k)-G(k-1)}\big)\frac{t_k}{\ln k}\\)

Энд орсон \\(F(k)-F(k-1)\\) ба \\(G(k)-G(k-1)\\) илэрхийллүүдийг үнэлэхэд

\\(\displaystyle\sqrt{k}-\sqrt{k-1}=\frac1{\sqrt{k}+\sqrt{k-1}}<\frac1{2\sqrt{k-1}}\\)

\\(\displaystyle\ln k-\ln(k-1)=\ln\Big(1+\frac1{k-1}\Big)\leq\frac1{k-1}\\)

\\(\displaystyle\ln^2\!k-\ln^2(k-1)=\big(\ln k+\ln(k-1)\big)\ln\Big(1+\frac1{k-1}\Big)\leq\frac{2\ln k}{k-1}\\)

тэнцэл бишүүд хэрэг болно. Баруун гар талд нь байгаа функцүүд бүгд \\(k\geq2\\) хувьсагчийн буурах функцүүд байгааг ажиглаарай. Ингээд

\\(\displaystyle G(k)-G(k-1)<\frac65A+\frac{5}{2\ln6}\cdot\frac{\ln k}{k-1}+\frac5{2(k-1)}\\)

\\(\displaystyle F(k)-F(k-1)>A-\frac{6A}{5\sqrt{k-1}}-\frac{5}{4\ln6}\cdot\frac{\ln k}{k-1}-\frac{15}{4(k-1)}\\)

гэсэн үнэлгээ гарна. Тухайлбал, \\(k\geq m\\) үед

\\(\displaystyle G(k)-G(k-1)<2,\qquad F(k)-F(k-1)>\frac12\\)

байдаг \\(m\\) гэсэн индекс олдоно (Үүнд \\(m=30\\) гэж авахад хангалттай).

[![](/blog/assets/wp-media/2018/05/ffgg-e1526569850231.png)](https://t8m8r.wordpress.com/wp-content/uploads/2018/05/ffgg.png)

Одоо \\(\sum{t_n}/{\ln n}\\) цуваа нийлдэг бөгөөд

\\(\displaystyle \sum_{k=2}^\infty\frac{t_k}{\ln k}=M\\)

болог. Тэгвэл 

\\(\displaystyle \sum_{p\leq n}t_p<\frac{G(2)t_2}{\ln2}+\sum_{k=3}^n\big({G(k)-G(k-1)}\big)\frac{t_k}{\ln k}
тул \\(\sum{t_p}\\) цуваа нийлэх нь тодорхой. Нөгөө талаас, \\(\sum{t_n}/{\ln n}\\) цуваа сарнидаг гэвэл

\\(\displaystyle \sum_{p\leq n}t_p>\frac{F(2)t_2}{\ln 2}+\sum_{k=3}^n\big({F(k)-F(k-1)}\big)\frac{t_k}{\ln k}>c+\frac12\sum_{k=m}^n\frac{t_k}{\ln k}\to\infty\\)

болох тул \\(\sum{t_p}\\) цуваа сарнина. Ингээд теорем батлагдлаа.

**Дасгал.** Дараах цувааг нийлэх эсэхийг тогтоо.

\\(\displaystyle\sum_p\frac1{p(\ln p)^{\varepsilon}}\\)

Энд  \\(\varepsilon>0\\) нь бодит тоо.
