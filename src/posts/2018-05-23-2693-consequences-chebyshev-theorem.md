---
layout: "layouts/post.njk"
title: "Чебышёвын теоремын мөрдлөгөөнүүд"
date: "2018-05-23T17:58:31"
slug: "consequences-chebyshev-theorem"
permalink: "/2018/05/23/consequences-chebyshev-theorem/"
wordpress_id: 2693
wordpress_url: "https://t8m8r.wordpress.com/2018/05/23/consequences-chebyshev-theorem/"
categories: ["Анализ", "Тооны онол"]
tags: ["Гаусс", "Лежандр", "Чебышёв", "анхны тооны тархалт"]
status: "publish"
comments_count: 0
math: true
generated_by: "wordpress-importer"
templateEngineOverride: "md"
---

[Өмнөх постоороо](/blog/2018/05/23/chebyshev-fundamental-theorem/) бид Чебышёвын онолын дараах тулгуур теоремыг баталсан.

**Теорем.** Хичнээн ч том бүхэл тоо \\(k\\), хичнээн ч бага бодит тоо \\(\alpha>0\\) өгөгдсөн байсан,

\\(\displaystyle\pi(n)<\mathrm{Li}(n)+\frac{\alpha n}{\ln^k\!n}\\)

байх төгсгөлгүй олон индекс \\(n\\) олдоно. Түүнчлэн,

\\(\displaystyle\pi(n)>\mathrm{Li}(n)-\frac{\alpha n}{\ln^k\!n}\\)

тэнцэл биш төгсгөлгүй олон \\(n\\)-ийн хувьд биелнэ. Өөрөөр хэлбэл дурын \\(k\\) бүхэл тооны хувьд

\\(\displaystyle\liminf_{n\to\infty}\big(\pi(n)-\mathrm{Li}(n)\big)\frac{\ln^k\!n}n\leq0,\qquad\limsup_{n\to\infty}\big(\pi(n)-\mathrm{Li}(n)\big)\frac{\ln^k\!n}n\geq0.\\)

Одоо үүнээс гарах зарим чухал мөрдлөгөөнүүдийг авч үзье.

**Мөрдлөгөө 1.** Хэрэв

\\(\displaystyle\lim_{n\to\infty}\frac{\pi(n)\ln n}{n},\qquad\lim_{n\to\infty}\frac{\pi(n)(\ln n-1.08366)}{n},\qquad\lim_{n\to\infty}\frac{\pi(n)}{\mathrm{Li}(n)}\\)

хязгааруудын аль нэг нь л оршин байдаг бол, бусад нь мөн оршин байх бөгөөд, утга нь бүгд 1-тэй тэнцүү байх ёстой. Иймд [Гаусс-Лежандрын таамаглалыг](/blog/2018/05/15/pnt/) батлахын тулд энэ хязгаар оршин байхыг харуулах л үлдэнэ.

**Баталгаа.** Ямар ч \\(\beta\\) тогтмолын хувьд

\\(\displaystyle \lim_{x\to\infty}\frac{{x}/{(\ln x+\beta)}}{\mathrm{Li}(x)}=\lim_{x\to\infty}\frac{\frac1{\ln x+\beta}-\frac{x}{(\ln x+\beta)^2}\cdot\frac1x}{\frac1{\ln x}}=1\\)

тул

\\(\displaystyle\lim_{n\to\infty}\frac{\pi(n)(\ln n+\beta)}{n}=L\qquad\Longleftrightarrow\qquad\lim_{n\to\infty}\frac{\pi(n)}{\mathrm{Li}(n)}=L.\\)

Одоо энэ хязгаар оршин байдаг бөгөөд утга нь \\(L\\)-тэй тэнцүү, өөрөөр хэлбэл \\(\varepsilon>0\\) тоо хичнээн ч бага байсан \\(n\\) хангалттай их л бол

\\(\displaystyle L-\varepsilon<\frac{\pi(n)}{\mathrm{Li}(n)}
байдаг гэж үзье. Тухайлбал, \\(L>1\\) бол \\(\varepsilon=\frac{L-1}2\\) гэж сонгож авснаар хангалттай их бүх \\(n\\)-ийн хувьд

\\(\displaystyle \frac{\pi(n)}{\mathrm{Li}(n)}>L-\varepsilon=\frac{L+1}2=1+\varepsilon\\)

гэж гарна. Энэ нь жишээлбэл төгсгөлгүй олон \\(n\\)-ийн хувьд

\\(\displaystyle\pi(n)<\mathrm{Li}(n)+\frac{n}{\ln^2\!n}\\)

байна гэдэгт харшлах тул \\(L>1\\) байж болохгүй. Үүнтэй төстэйгөөр, \\(L<1\\) байж болохгүй гэдгийг харуулна. Мөрдлөгөө батлагдлаа.

Анхны тоонуудын тархалтын талаар

\\(\displaystyle\pi(n)\approx\frac{n}{\ln n-1.08366}\\)

гэсэн таамаглал [Лежандр дэвшүүлснийг](/blog/2018/05/15/pnt/) бид мэднэ. Үүнийг эхний ээлжинд

\\(\displaystyle\lim_{n\to\infty}\frac{\pi(n)(\ln n-1.08366)}{n}=1\\)

гэж тайлбарлаж болох бөгөөд энэ нь

\\(\displaystyle\lim_{n\to\infty}\frac{\pi(n)}{\mathrm{Li}(n)}=1\\)

гэсэн Гауссын таамаглалтай эквивалент. Эдгээрийг хамтад нь бид «Гаусс-Лежандрын таамаглал», эсвэл «анхны тооны теорем» гэж яриад байгаа.

Гэвч дээрх тайлбар Лежандрын таамаглалд байгаа 1.08366 гэсэн тогтмолын учрыг тайлбарлахад хүчин мөхөстөнө. Үүний тулд

\\(\displaystyle\pi(n)=\frac{n}{\ln n+\beta(n)}\\)

харьцаагаар \\(\beta(n)\\) гэсэн функц тодорхойлоод,

\\(\displaystyle\lim_{n\to\infty}\beta(n)=-1.08366\\)

буюу

\\(\displaystyle\lim_{n\to\infty}\Big(\frac{n}{\pi(n)}-\ln n\Big)=-1.08366\\)

гэсэн дараагийн шатны (арай нарийн) таамаглал дэвшүүлж болно. Чебышёв өөрийн теоремыг хэрэглэн энэ таамаглалд засвар хэрэгтэй гэдгийг харуулсан.

**Мөрдлөгөө 2.** Хэрэв

\\(\displaystyle\lim_{n\to\infty}\Big(\frac{n}{\pi(n)}-\ln n\Big)\\)

хязгаар оршин байдаг бол утга нь (–1)-тэй тэнцүү байх ёстой.

**Баталгаа.** Дээрх хязгаар оршин байдаг бөгөөд утга нь \\(B\\)-тэй тэнцүү, ө.х.

\\(\displaystyle\lim_{n\to\infty}\Big(\frac{n}{\pi(n)}-\ln n\Big)=B\qquad(*)\\)

гэж үзье. Иймд \\(\varepsilon>0\\) тоо хичнээн ч бага байсан \\(n\\) хангалттай их л бол

\\(\displaystyle B-\varepsilon<\frac{n}{\pi(n)}-\ln n
байна. Энэ тэнцэл бишүүдийг \\((\ln n)\\)-д хуваавал

\\(\displaystyle \frac{B-\varepsilon}{\ln n}<\frac{n}{\pi(n)\ln n}-1<\frac{B+\varepsilon}{\ln n}\\)

гарах тул юуны өмнө

\\(\displaystyle \lim_{n\to\infty}\frac{\pi(n)\ln n}{n}=1\qquad(\dagger)\\)

гэж мөрдөнө. Тэгэхээр (*) нь Гаусс-Лежандрын таамаглалаас илүү хүчтэй таамаглал гэсэн үг.

Одоо \\(B>-1\\) гэж үзээд, (**) тэнцэл бишид \\(B-\varepsilon=-1+\delta<0\\) ба \\(\delta>0\\) байхаар \\(\varepsilon\\) параметрийг сонговол

\\(\displaystyle \frac{n}{\ln n}-\pi(n)>(B-\varepsilon)\frac{\pi(n)}{\ln n}=(-1+\delta)\frac{\pi(n)}{\ln n}\\)

гарна. Нөгөө талаас, \\((\dagger)\\) томъёоноос, \\(n\\) хангалттай их үед

\\(\displaystyle \pi(n)<(1+\delta)\frac{n}{\ln n}\\)

тул

\\(\displaystyle \frac{n}{\ln n}-\pi(n)>(-1+\delta)\frac{\pi(n)}{\ln n}>(-1+\delta^2)\frac{n}{\ln^2\!n}\\)

буюу

\\(\displaystyle\pi(n)-\frac{n}{\ln n}-\frac{n}{\ln^2\!n}<-\delta^2\frac{n}{\ln^2\!n}\qquad(\dagger\dagger)\\)

гэж дүгнэж болно. Үүнийг теоремтойгоо холбохын тулд

\\(\displaystyle\mathrm{Li}(x)=\frac{x}{\ln x}+\frac{x}{\ln^2\!x}+O\Big(\frac{x}{\ln^3\!x}\Big)\\)

гэсэн [үр дүнг](/blog/2018/05/15/pnt/) санацгаая. Тухайлбал,

\\(\displaystyle\frac{n}{\ln n}+\frac{n}{\ln^2\!n}-\mathrm{Li}(n)
байх \\(C\\) тогтмол олдоно. Энэ тэнцэл бишийг \\((\dagger\dagger)\\) дээр нэмбэл хангалттай их бүх \\(n\\)-ийн хувьд

\\(\displaystyle\pi(n)-\mathrm{Li}(n)<-\delta^2\frac{n}{\ln^2\!n}+C\frac{n}{\ln^3\!n}\\)

болох тул жишээлбэл төгсгөлгүй олон \\(n\\)-ийн хувьд

\\(\displaystyle\pi(n)-\mathrm{Li}(n)>-\frac{n}{\ln^3\!n}\\)

байна гэдэгт харшилж, \\(B>-1\\) байж болохгүй нь харагдана. Үүнтэй төстэйгөөр, \\(B<-1\\) байж болохгүй. Мөрдлөгөө батлагдлаа.

Дээрх баталгаануудаас нэг ажиглалт хийхэд, эхний мөрдлөгөөний баталгаанд

\\(\displaystyle\pi(n)-\mathrm{Li}(n)<\frac{n}{\ln^2\!n}\\)

тэнцэл биш зөвхөн төгсгөлөг тооны \\(n\\)-ийн хувьд биелэхэд хүрч, зөрчил үүсгэж байсан бол хоёрдахь мөрдлөгөөний баталгаанд

\\(\displaystyle\pi(n)-\mathrm{Li}(n)<\frac{n}{\ln^3\!n}\\)

тэнцэл биш төстэй үүрэг гүйцэтгэсэн. Үүний цаад учир нь юу вэ гэвэл, 1-рт, хэрэв \\(f(n)\\) функц

\\(\displaystyle \pi(n)-f(n)=O\Big(\frac{n}{\ln^k\!n}\Big)\\)

шинж чанартай бол

\\(\displaystyle f(n)=\mathrm{Li}(n)+O\Big(\frac{n}{\ln^k\!n}\Big)\\)

байхаас өөр аргагүй, 2-рт,

\\(\displaystyle\mathrm{Li}(n)=\frac{n}{\ln n}+\frac{n}{\ln^2\!n}+\frac{2n}{\ln^3\!n}+\ldots+\frac{(k-1)!n}{\ln^{k}\!n}+O\Big(\frac{n}{\ln^{k+1}\!n}\Big)\\)

гэсэн задаргаа биелдэг явдал юм. Жишээлбэл

\\(\displaystyle\frac{n}{\ln n-A}=\frac{n}{\ln n}+\frac{An}{\ln^2\!n}+\frac{A^2n}{\ln^3\!n}+O\Big(\frac{n}{\ln^4\!n}\Big)\\)

задаргаа \\(A=1\\) үед дээрх задаргаатай эхний 2 гишүүнээрээ, \\(A\neq1\\) үед зөвхөн эхний ганц гишүүнээрээ нийцтэй. Иймд \\(A\neq1\\) үед

\\(\displaystyle \pi(n)=\frac{n}{\ln n-A}+O\Big(\frac{n}{\ln^2\!n}\Big)\\)

байх боломжтой боловч

\\(\displaystyle \pi(n)=\frac{n}{\ln n-A}+O\Big(\frac{n}{\ln^3\!n}\Big)\\)

байх боломжгүй. Харин

\\(\displaystyle \pi(n)=\frac{n}{\ln n-1}+O\Big(\frac{n}{\ln^3\!n}\Big)\\)

байх боломжтой боловч

\\(\displaystyle \pi(n)=\frac{n}{\ln n-1}+O\Big(\frac{n}{\ln^4\!n}\Big)\\)

байх боломжгүй.

Дээрх ажиглалтыг эмхэтгэж бичье.

**Мөрдлөгөө 3.** Хэрэв

\\(\displaystyle\lim_{n\to\infty}\Big(f(n)-\mathrm{Li}(n)\Big)\frac{\ln^k\!n}n\neq0\\)

өөрөөр хэлбэл

\\(\displaystyle f(n)-\mathrm{Li}(n)\neq o\Big(\frac{n}{\ln^{k}\!n}\Big)\\)

бол

\\(\displaystyle\pi(n)=f(n)+O\Big(\frac{n}{\ln^{k+1}\!n}\Big)\\)

байх боломжгүй.

**Баталгаа. ** Ерөнхий чанарыг алдалгүйгээр

\\(\displaystyle\lim_{n\to\infty}\Big(f(n)-\mathrm{Li}(n)\Big)\frac{\ln^k\!n}n<0\\)

гэж үзье. Тэгвэл \\(n\\) хангалттай их үед

\\(\displaystyle f(n)-\mathrm{Li}(n)<-\frac{\alpha n}{\ln^k\!n}\\)

байх \\(\alpha>0\\) тогтмол олдоно. Нөгөө талаас,

\\(\displaystyle\pi(n)=f(n)+O\Big(\frac{n}{\ln^{k+1}\!n}\Big)\\)

гэдгээс ямар нэг \\(C\\) тогтмолын хувьд

\\(\displaystyle\pi(n)-f(n)<\frac{Cn}{\ln^{k+1}\!n}\\)

байна гэж гарна. Одоо хоёр тэнцэл бишээ хооронд нэмснээр

\\(\displaystyle\pi(n)-\mathrm{Li}(n)<-\frac{\alpha n}{\ln^k\!n}+\frac{Cn}{\ln^{k+1}\!n}\\)

болж, төгсгөлгүй олон \\(n\\)-ийн хувьд

\\(\displaystyle\pi(n)-\mathrm{Li}(n)>-\frac{n}{\ln^{k+1}\!n}\\)

гэсэн тулгуур теоремын үр дүнтэй зөрчилдөнө.

**Дасгал.** Өмнөх мөрдлөгөөг ашиглан,

\\(\displaystyle\pi(n)=f(n)+O\Big(\frac{n}{\ln^{4}\!n}\Big)\\)

байх боломжтой

\\(\displaystyle f(n)=\frac{n\ln n}{\ln^2\!n-\ln n+c}\\)

хэлбэрийн бүх функцийг ол. Өөрөөр хэлбэл,

\\(\displaystyle \lim_{n\to\infty}\Big(\frac{n}{\pi(n)}-\ln n+1\Big)\ln n\\)

хязгаар оршин байдаг бол, утга нь хэд байх ёстой вэ?

[![](/blog/assets/wp-media/2018/05/gamlim-e1527098153559.png)](https://t8m8r.wordpress.com/wp-content/uploads/2018/05/gamlim.png)
