---
layout: "layouts/post.njk"
title: "Чебышёвын тулгуур теорем"
date: "2018-05-23T04:40:24"
slug: "chebyshev-fundamental-theorem"
permalink: "/2018/05/23/chebyshev-fundamental-theorem/"
wordpress_id: 2684
wordpress_url: "https://t8m8r.wordpress.com/2018/05/23/chebyshev-fundamental-theorem/"
categories: ["Анализ", "Тооны онол"]
tags: ["Чебышёв", "анхны тоо", "анхны тооны тархалт"]
status: "publish"
comments_count: 0
math: true
generated_by: "wordpress-importer"
templateEngineOverride: "md"
---

[Өмнөх постоороо](/blog/2018/05/22/prime-zeta/) бид \\(s>1\\) мужид тодорхойлогдсон

\\(\displaystyle f_6(s)=P(s)+Z(s)\\)

функцийн бүх зэргийн уламжлал \\(s\to1\\) хязгаарт төгсгөлөг утгатай байна гэдгийг харуулсан. Үүнд

\\(\displaystyle P(s)=\sum_p\frac1{p^s}\\)

нь «анхны тоон зета функц» гэгддэг функц бол

\\(\displaystyle Z(s)=-\sum_{n\geq2}\frac1{n^s\ln n}\\)

нь \\(Z'(s)=\zeta(s)-1\\) тэнцлийг хангах тул зета функцийн эх функцтэй их ойрын хамаатан. Анхны тоон зета функцийг

\\(\displaystyle P(s)=\sum_p\frac1{p^s}=\sum_{n\geq2}\frac{\pi(n)-\pi(n-1)}{n^s}\\)

гэж бичвэл

\\(\displaystyle f_6(s)=P(s)+Z(s)=\sum_{n\geq2}\Big(\pi(n)-\pi(n-1)-\frac1{\ln n}\Big)\frac1{n^s}\\)

болно. Үүнээсээ цааш нь уламжлал авбал

\\(\displaystyle f_6^{(k)}(s)=(-1)^k\sum_{n\geq2}\Big(\pi(n)-\pi(n-1)-\frac1{\ln n}\Big)\frac{\ln^k\!n}{n^s}.\\)

Тэгэхээр өмнөх постны үр дүнг дараах маягаар томъёолж бас болно.

**Теорем.** Ямар ч \\(k\geq0\\) бүхэл тооны хувьд \\(s>1\\) мужид тодорхойлогдсон

\\(\displaystyle g_k(s)=\sum_{n\geq2}\Big(\pi(n)-\pi(n-1)-\frac1{\ln n}\Big)\frac{\ln^k\!n}{n^s}\qquad(*)\\)

функц \\(s\to1\\) хязгаарт төгсгөлөг утгатай.

Хаалтанд байгаа \\(\frac1{\ln n}\\) гишүүнийг

\\(\displaystyle \frac1{\ln n}=L(n)-L(n-1)\qquad(**)\\)

хэлбэрт бичихийн тулд

\\(\displaystyle L(n)=\sum_{j=2}^{n}\frac1{\ln j}\\)

гэсэн функц тодорхойлж болно. Чебышёв үүний оронд (аргумент нь бодит тоо байж болдог)

\\(\displaystyle \mathrm{Li}(x)=\int_2^x\frac{dt}{\ln t}\\)

функцийг илүүд үзсэн бөгөөд дээрх теорем дахь (**) гишүүнийг

\\(\displaystyle \mathrm{Li}(n)-\mathrm{Li}(n-1)=\int_{n-1}^n\frac{dt}{\ln t}\\)

илэрхийллээр сольсон. Энэ тэнцэтгэлийн баруун гар талын интеграл \\(n=2\\) үед сарних тул нэг бол \\(\mathrm{Li}(1)=0\\) гэж хүчээр тодорхойлох, эсвэл (*) нийлбэрийг \\(n=2\\) биш арай их индексээс эхлэх хэрэгтэй.

**Мөрдлөгөө.** Ямар ч \\(k\geq0\\) бүхэл тооны хувьд \\(s>1\\) мужид тодорхойлогдсон

\\(\displaystyle h_k(s)=\sum_{n\geq3}\Big(\pi(n)-\pi(n-1)-\int_{n-1}^n\frac{dt}{\ln t}\Big)\frac{\ln^k\!n}{n^s}\qquad(\dagger)\\)

функц \\(s\to1\\) хязгаарт төгсгөлөг утгатай.

**Баталгаа.** Дээрх теоремын (*) нийлбэрийг \\(n=3\\) индексээс эхлүүлээд (ө.х. нийлбэрийн хамгийн эхний нэмэгдэхүүнийг хаяад) \\(g_k(s)\\) функцийг шинээр тодорхойлбол теорем хүчинтэй хэвээр үлдэх нь мэдээж. Ингээд \\((*)\\) ба \\((\dagger)\\) илэрхийллүүдийн ялгаврыг олбол

\\(\displaystyle\Delta(s)=h_k(s)-g_k(s)=\sum_{n\geq3}\Big(\frac1{\ln n}-\int_{n-1}^n\frac{dt}{\ln t}\Big)\frac{\ln^k\!n}{n^s}.\\)

Үүнийг зааглахын тулд логарифм нь өсөх функц гэдгийг тооцвол

\\(\displaystyle \frac1{\ln n}<\int_{n-1}^n\frac{dt}{\ln t}<\frac1{\ln(n-1)}\\)

буюу

\\(\displaystyle \Big|\frac1{\ln n}-\int_{n-1}^n\frac{dt}{\ln t}\Big|<\frac1{\ln(n-1)}-\frac1{\ln n}=\frac{\ln n-\ln(n-1)}{\ln(n-1)\ln n}=\frac{\ln(1+\frac1{n-1})}{\ln(n-1)\ln n}\\)

гарна. Одоо \\(0\leq x\leq1\\) үед \\(\ln(1+x)\leq x\\) тэнцэл бишээс

\\(\displaystyle \Big|\frac1{\ln n}-\int_{n-1}^n\frac{dt}{\ln t}\Big|<\frac1{(n-1)\ln(n-1)\ln n}<\frac2n\\)

гэж мөрдөх ба үүнийгээ ашиглан

\\(\displaystyle|\Delta(s)|=|h_k(s)-g_k(s)|<\sum_{n\geq3}\frac{2\ln^k\!n}{n^{1+s}}\\)

заагт хүрнэ. Эндээс \\(\Delta(s)\\) ялгавар \\(s\to1\\) хязгаарт төгсгөлөг утгатай гэдэг нь тодорхой. Эцэст нь

\\(h_k(s)=g_k(s)+\Delta(s)\\)

тэнцлийг санавал \\(h_k(s)\\) функц \\(s\to1\\) хязгаарт төгсгөлөг утгатай болж, баталгаа дуусна.

Одоо

\\(\displaystyle a_n=\pi(n)-\mathrm{Li}(n),\qquad b_n=\frac{\ln^k\!n}{n^s}\\)

тэмдэглэгээнүүдийг ашиглан \\((\dagger)\\) илэрхийллийг

\\(\displaystyle h_k(s)=\sum_{n\geq3}(a_n-a_{n-1})b_n=\lim_{m\to\infty}\sum_{n=3}^m(a_n-a_{n-1})b_n\\)

гэж бичиж болно. Энэ хэсэгчилсэн нийлбэрийг цааш нь

\\(\displaystyle h_{k,m}(s)=\sum_{n=3}^m(a_n-a_{n-1})b_n=\sum_{n=3}^ma_nb_n-\sum_{n=2}^{m-1}a_nb_{n+1}\\{}\qquad=a_mb_m-a_2b_3+\sum_{n=3}^{m-1}a_n(b_n-b_{n+1})\\)

маягаар ([Абелийн хувиргалтаар](/blog/2018/05/20/abel-summation/)) хувиргавал

\\(\displaystyle h_k(s)=-a_2b_3+\lim_{m\to\infty}\Big(a_mb_m+\sum_{n=3}^{m-1}a_n(b_n-b_{n+1})\Big).\\)

Хязгаар дотор байгаа \\(a_mb_m\\) гишүүнийг түр мартаад,

\\(\displaystyle b_n-b_{n+1}\approx \frac{\ln^k\!n}{n^s}-\frac{\ln^k\!n}{(n+1)^s}\approx\frac{\ln^k\!n}{n^{s}}\Big(1-\big(1+\frac1n\big)^{-s}\Big)\approx\frac{s\ln^k\!n}{n^{1+s}}\\)

гэж бүдүүвчилбэл, \\(s\to1\\) үед

\\(\displaystyle h_k(s)\sim\sum_{n\geq3}\big(\pi(n)-\mathrm{Li}(n)\big)\frac{\ln^k\!n}{n^{1+s}}\qquad(\dagger\dagger)\\)

нийлбэр төгсгөлөг утгатай. Тэгэхээр \\(\pi(n)-\mathrm{Li}(n)\\) ялгавар \\(n\to\infty\\) үед \\(n^{1-\varepsilon}\\) хэлбэрийн хэмжигдэхүүнээр зааглагдахгүй, их утга авдаг бол энэ их утган дотор эерэг ч сөрөг ч утга төгсгөлгүй олон тохиолдох ёстой. Өөрөөр хэлбэл \\(\pi(n)-\mathrm{Li}(n)\\) ялгавар [Гаусс-Лежандрын таамаглалыг](/blog/2018/05/15/pnt/) худлаа болгохоор тийм их байдаг бол, зөвхөн нэг тийшээ хэлбийсэн байж болохгүй, дээшээ доошоо байн байн хэлбэлзсэн маягтай байх хэрэгтэй болно. Энэ санааг хэрэгжүүлснээр бид Чебышёвын тулгуур теоремд хүрнэ.

**Тэмдэглэл.** Чебышёвын теоремыг батлахын өмнө \\((\dagger\dagger)\\) томъёоноос

\\(\pi(n)-\mathrm{Li}(n)=o(\mathrm{Li}(n))\\)

хэлбэрийн заагийг гаргаж болохгүй юм уу гэсэн асуултыг авч үзье. Хэрэв тэгж чадвал Гаусс-Лежандрын таамаглал шууд батлагдана. Энд юу саад болж байна вэ гэвэл \\(\pi(n)-\mathrm{Li}(n)\\) ялгавар хаа нэгтээ \\(A\\) гэсэн том утга авсныгаа дараа нь хаа нэгтээ \\(-A\\) гэсэн утга аваад «засчихыг» бид байг гэж чадахгүй. Жишээлбэл \\((\dagger\dagger)\\) томъёонд \\(\pi(n)-\mathrm{Li}(n)=(-1)^nn\\) гэвэл

\\(\displaystyle h_k(s)\sim\sum_{n\geq3}\frac{(-1)^n\ln^k\!n}{n^{s}}\sim-\sum_{n\geq2}\frac{s\ln^k(2n)}{(2n)^{1+s}}\\)

болох тул \\(s\to1\\) хязгаарыг авахад ямар ч төвөг учрахгүй.

**Теорем.** Хичнээн ч том бүхэл тоо \\(k\\), хичнээн ч бага бодит тоо \\(\alpha>0\\) өгөгдсөн байсан,

\\(\displaystyle\pi(n)<\mathrm{Li}(n)+\frac{\alpha n}{\ln^k\!n}\\)

байх төгсгөлгүй олон индекс \\(n\\) олдоно. Түүнчлэн, 

\\(\displaystyle\pi(n)>\mathrm{Li}(n)-\frac{\alpha n}{\ln^k\!n}\\)

тэнцэл биш төгсгөлгүй олон \\(n\\)-ийн хувьд биелнэ. Өөрөөр хэлбэл дурын \\(k\\) бүхэл тооны хувьд

\\(\displaystyle\liminf_{n\to\infty}\big(\pi(n)-\mathrm{Li}(n)\big)\frac{\ln^k\!n}n\leq0,\qquad\limsup_{n\to\infty}\big(\pi(n)-\mathrm{Li}(n)\big)\frac{\ln^k\!n}n\geq0.\\)

[![](/blog/assets/wp-media/2018/05/chebnd.png)](/blog/assets/wp-media/2018/05/chebnd.png) Гауссын \\(G(x)=\frac{x}{\ln x}\\) ба \\(\mathrm{Li}(x)\\), мөн Лежандрын \\(L(x)=\frac{x}{\ln x-1.08366}\\) ойролцооллуудын алдааг Чебышёвын төрлийн \\(\frac{x}{\ln^5\!x}\\) заагтай харьцуулсан нь.

**Баталгаа.** Эхлээд \\(k\\) бүхэл тоо, \\(\alpha>0\\) бодит тоогоо сонгож аваад,

\\(\displaystyle\pi(n)<\mathrm{Li}(n)+\frac{\alpha n}{\ln^k\!n}\\)

тэнцэл биш зөвхөн төгсгөлөг тооны \\(n\\)-ийн хувьд л биелдэг, өөрөөр хэлбэл тодорхой нэг утгаас эхлээд бүх \\(n\\)-ийн хувьд

\\(\displaystyle a_n=\pi(n)-\mathrm{Li}(n)\geq\frac{\alpha n}{\ln^k\!n}\qquad(\ddagger)\\)

байдаг гэж үзье. Нөгөө талаас, дундаж утгын тухай теоремоор

\\(\displaystyle b_n-b_{n+1}=\frac{\ln^k\!n}{n^s}-\frac{\ln^k(n+1)}{(n+1)^s}=\Big(s-\frac{k}{\ln(n+\theta_n)}\Big)\frac{\ln^k(n+\theta_n)}{(n+\theta_n)^{1+s}}\\)

байх \\(0<\theta_n<1\\) олдоно. Баруун гар тал дахь илэрхийллийг жаахан хялбарчлая. Юуны түрүүнд \\(s>1\\) ба логарифм нь өсөх функц тул \\(n\\) хангалттай их үед

\\(\displaystyle s-\frac{k}{\ln(n+\theta_n)}>\frac1{\sqrt2}\\)

ба

\\(\displaystyle \frac{\ln^k(n+\theta_n)}{(n+\theta_n)^{1+s}}\geq\frac{\ln^k\!n}{(n+\theta_n)^{1+s}}\geq\frac{\ln^k\!n}{\sqrt2n^{1+s}}.\\)

Эдгээрийг эмхэтгэж бичвэл

\\(\displaystyle b_n-b_{n+1}\geq\frac{\ln^k\!n}{2n^{1+s}}.\qquad(\ddagger\ddagger)\\)

Одоо \\(n\geq r\\) үед \\((\ddagger)\\) ба \\((\ddagger\ddagger)\\) тэнцэл бишүүд зэрэг биелдэг гэвэл, \\(a_mb_m>0\\) гэдгийг тооцон

\\(\displaystyle h_{k,m}(s)=a_mb_m\underbrace{-a_2b_3+\sum_{n=3}^{r-1}a_n(b_n-b_{n+1})}_{C}+\sum_{n=r}^{m-1}a_n(b_n-b_{n+1})\\{}\qquad> C+\sum_{n=r}^{m-1}\frac{\alpha n}{\ln^k\!n}\cdot\frac{\ln^k\!n}{2n^{1+s}}=C+\sum_{n=r}^{m-1}\frac{\alpha}{2n^{s}}\\)

болох тул \\(s\to1\\) үед

\\(\displaystyle h_k(s)=\lim_{m\to\infty}h_{k,m}(s)\geq C-\sum_{n=1}^{r-1}\frac{\alpha}{2n^{s}}+\zeta(s)\to\infty.\\)

Энэ нь \\(h_k(s)\\) функц \\(s\to1\\) хязгаарт төгсгөлөг утгатай гэсэн мөрдлөгөөтэй харшилж, теоремын эхний хагас батлагдана.

Хоёрдахь хагасынх нь баталгаа эхний хагасынхтайгаа адилхан тул товчхон сийрүүлье. Бүх \\(n\geq r\\)-ийн хувьд

\\(\displaystyle a_n=\pi(n)-\mathrm{Li}(n)\leq-\frac{\alpha n}{\ln^k\!n}\\)

байдаг гэж үзсэнээр эхэлнэ. Эндээс \\(a_mb_m<0\\) гэдгийг тооцон

\\(\displaystyle h_{k,m}(s)=a_mb_m\underbrace{-a_2b_3+\sum_{n=3}^{r-1}a_n(b_n-b_{n+1})}_{C}+\sum_{n=r}^{m-1}a_n(b_n-b_{n+1})\\{}\qquad< C-\sum_{n=r}^{m-1}\frac{\alpha n}{\ln^k\!n}\cdot\frac{\ln^k\!n}{2n^{1+s}}=C-\sum_{n=r}^{m-1}\frac{\alpha}{2n^{s}}\\)

гэж гарах ба \\(s\to1\\) үед

\\(\displaystyle h_k(s)=\lim_{m\to\infty}h_{k,m}(s)\leq C+\sum_{n=1}^{r-1}\frac{\alpha}{2n^{s}}-\zeta(s)\to-\infty.\\)

Теорем бүрэн батлагдлаа.
