---
layout: "layouts/post.njk"
title: "Караматын тэнцэл биш"
date: "2021-01-05T22:51:58"
slug: "karamata-inequality"
permalink: "/2021/01/05/karamata-inequality/"
wordpress_id: 4893
wordpress_url: "https://t8m8r.wordpress.com/2021/01/05/karamata-inequality/"
categories: ["Анализ", "Тэнцэл биш"]
tags: ["Йенсен", "Карамата", "Караматын тэнцэл биш", "Фукс", "хашилт"]
status: "publish"
comments_count: 0
math: true
generated_by: "wordpress-importer"
templateEngineOverride: "md"
---

[Кошийн](/blog/2020/12/03/amgm/) тэнцэл бишийг [Мюрхедийн](/blog/2020/12/25/muirhead-inequality/) тэнцэл биш яаж өргөтгөж байсантай төстэйгөөр [Йенсений](/blog/2020/12/31/jensen-inequality/) тэнцэл бишийг өргөтгөдөг нэгэн тэнцэл биш байдаг. Энд Мюрхедийн тэнцэл биштэй холбоотой орж ирсэн *нэг вектор нөгөөгөө хаших* гэсэн ойлголт тулгуур байр суурь эзэлнэ.

**Тодорхойлолт 1.**  Хэрэв \({x=(x_1,\ldots,x_n)}\) ба \({y=(y_1,\ldots,y_n)}\) векторын байгуулагчид \({x_1\geq\ldots\geq x_n}\) ба \({y_1\geq\ldots\geq y_n}\) байхаар эрэмбэлэгдсэн бөгөөд, 

\(\displaystyle  \begin{array}{rcl}  x_1&\leq&y_1,\\ x_1+x_2&\leq&y_1+y_2,\\ \ldots&&\ldots\\ x_1+\ldots+x_{n-1}&\leq&y_1+\ldots+y_{n-1},\\ x_1+\ldots+x_{n}&=&y_1+\ldots+y_{n}, \end{array}\)

 нөхцлийг хангадаг бол, \({x}\) вектор \({y}\) вектороор *хашигдаж* байна гээд \({x\prec y}\) гэж бичнэ. Ерөнхий тохиолдолд \({x}\), \({y}\) векторын байгуулагчдыг эрэмбэлэхэд гарах хоёр векторыг \({x'}\), \({y'}\) гэвэл, хэрэв \({x'\prec y'}\) бол \({x}\) вектор \({y}\) вектороор *хашигдаж* байна гээд \({x\prec y}\) гэж тэмдэглэдэг. 

Дараах үр дүнг [1932 онд](http://elib.mi.sanu.ac.rs/files/journals/publ/1/11.pdf) Сербийн математикч [Йован Карамата](https://en.wikipedia.org/wiki/Jovan_Karamata) анх баталсан бөгөөд *Караматын* тэнцэл биш, *хашилтын* тэнцэл биш, эсвэл *Харди-Литлвудын* тэнцэл биш зэрэг нэрээр алдаршжээ.

 

**Теорем 2.**  Хоёр вектор \({x,y\in[a,b]^n}\) өгөгдсөн үед \({x\prec y}\) байх зайлшгүй бөгөөд хүрэлцээтэй нөхцөл нь \({[a,b]}\) завсар дээрх гүдгэр функц \({f}\) болгоны хувьд [

\(\displaystyle  f(x_1)+\ldots+f(x_n) \leq f(y_1)+\ldots+f(y_n) \ \ \ \ \ (1)\)

] тэнцэл биш биелэх явдал юм. Цаашилбал, хэрэв \({f}\) нь эрс гүдгэр бол энэ тэнцэл бишийн тэнцэлдээ хүрэх зайлшгүй нөхцөл нь \({x_1=y_1,\ldots,x_n=y_n}\). 

Энэ теорем нь \({x\prec y}\) нөхцлөөс [(1)](#ekaramata) тэнцэл биш мөрдөнө гэж хэлээд зогсохгүй, \({x\prec y}\) нөхцлийг өөрийг нь [(1)](#ekaramata) тэнцэл бишийг ашиглан шалгах боломж өгч байгаа. Үнэндээ бол \({x\prec y}\) нөхцөл биелнэ гэж харуулахын тулд [(1)](#ekaramata) тэнцэл бишийг бүх гүдгэр функцийн хувьд шалгах шаардлага байхгүй. Бодит \({t}\) гэсэн параметр бүхий 

\(\displaystyle  f(x)=|x-t|\)

 хэлбэрийн функцүүдийн бүлийн хувьд шалгахад л хангалттай. *Хашилтын тэгшхэмт шинжүүр* гэгддэг энэ шинжүүрийн илүү ерөнхий хувилбарыг бид дор батална.

**Тэмдэглэл 3.**  Дээрх теоремд \({y_1\geq\ldots\geq y_n}\) өгөгдсөн гэж үзээд, 

\(\displaystyle  x_1=\ldots=x_n= z:= \frac{y_1+\ldots+y_n}n\)

 гэж авбал, мэдээж \({x_1+\ldots+x_n=nz=y_1+\ldots+y_n}\) байх бөгөөд 

\(\displaystyle  x_1=z\leq y_1,\quad x_1+x_2=2z\leq y_1+y_2,\quad \ldots\)

 тул \({x\prec y}\). Иймд, 

\(\displaystyle  nf(z)\leq f(y_1)+\ldots+f(y_n)\)

 буюу, Йенсений тэнцэл бишийн \({\lambda_1=\ldots=\lambda_n=\frac1n}\) жинтэй хувилбар мөрдөнө. 

Йенсений тэнцэл бишийн ерөнхий хувилбарыг өгч чадах Караматын «жинтэй» тэнцэл бишийг Унгарын математикч Ладислас Фукс [1947 онд](https://www.jstor.org/stable/24530530) баталжээ. Үүнд хашилтын харьцааг жин оруулан өргөтгөж тодорхойлох хэрэгтэй болдог.

**Теорем 4.**  Хэрэв \({f}\) нь \({[a,b]}\) завсар дээрх гүдгэр функц ба \({\lambda_1,\ldots,\lambda_n}\) нь бодит тоонууд бол 

\(\displaystyle  x_1\geq\ldots\geq x_n, \qquad y_1\geq\ldots\geq y_n,\)

 ба 

\(\displaystyle  \begin{array}{rcl}  \lambda_1x_1&\leq&\lambda_1y_1,\\ \lambda_1x_1+\lambda_2x_2&\leq&\lambda_1y_1+\lambda_2y_2,\\ \ldots&&\ldots\\ \lambda_1x_1+\ldots+\lambda_{n-1}x_{n-1}&\leq&\lambda_1y_1+\ldots+\lambda_{n-1}y_{n-1},\\ \lambda_1x_1+\ldots+\lambda_nx_{n}&=&\lambda_1y_1+\ldots+\lambda_ny_{n}, \end{array}\)

 байх \({x,y\in[a,b]^n}\) вектор болгоны хувьд [

\(\displaystyle  \lambda_1f(x_1)+\ldots+\lambda_nf(x_n) \leq \lambda_1f(y_1)+\ldots+\lambda_nf(y_n) \ \ \ \ \ (2)\)

] тэнцэл биш биелнэ. Цаашилбал, хэрэв \({f}\) нь эрс гүдгэр бөгөөд \({\lambda_1\cdots\lambda_n\neq0}\) бол энэ тэнцэл бишийн тэнцэлдээ хүрэх зайлшгүй нөхцөл нь \({x_1=y_1,\ldots,x_n=y_n}\). 

**Тэмдэглэл 5.**  Энэ теоремд \({y_1\geq\ldots\geq y_n}\) ба \({\lambda_1+\ldots+\lambda_n=1}\) байх эерэг \({\lambda_1,\ldots,\lambda_n}\) тоонууд өгөгдсөн гэж үзээд, 

\(\displaystyle  x_1=\ldots=x_n=z:= \lambda_1y_1+\ldots+\lambda_ny_n\)

 гэж авбал, мэдээж 

\(\displaystyle  \lambda_1x_1+\ldots+\lambda_nx_n =(\lambda_1+\ldots+\lambda_n)z =\lambda_1y_1+\ldots+\lambda_ny_n.\)

 Түүнчлэн, 

\(\displaystyle  \lambda_1x_1 = \lambda_1(\lambda_1y_1+\ldots+\lambda_ny_n) \leq \lambda_1(\lambda_1y_1+\lambda_2y_1+\ldots+\lambda_ny_1) \leq \lambda_1y_1,\)

 ба  

\(\displaystyle  \lambda_1x_1+\lambda_2x_2 = (\lambda_1+\lambda_2)(\lambda_1y_1+\ldots+\lambda_ny_n)\\ {}\qquad\qquad\quad\,\leq (\lambda_1+\lambda_2)(\lambda_1y_1+\lambda_2y_2)+(\lambda_1+\lambda_2)(\lambda_3\ldots+\lambda_n)y_3\\ {}\qquad\qquad\quad\,\leq \lambda_1(\lambda_1y_1+\lambda_2y_1+\lambda_3y_3+\ldots) +\lambda_2(\lambda_1y_2+\lambda_2y_2+\lambda_3y_3+\ldots)\\ {}\qquad\qquad\quad\,\leq \lambda_1y_1+\lambda_2y_2,\)

  гэх мэтчилэн 

\(\displaystyle  \lambda_1x_1+\ldots+\lambda_{n-1}x_{n-1} \leq \lambda_1y_1+\ldots+\lambda_{n-1}y_{n-1}\)

 тул теоремын нөхцөл биелнэ. Иймд, 

\(\displaystyle  f(z)\leq \lambda_1f(y_1)+\ldots+\lambda_nf(y_n)\)

 болж, Йенсений ерөнхий тэнцэл биш мөрдөнө. 

Дээр дурдагдсан тэгшхэмт шинжүүрийн «жинтэй» өргөтгөлийг одоо томъёолъё.

**Теорем 6 (Тэгшхэмт шинжүүр).**  Бодит тоон \({x_1\geq\ldots\geq x_n}\), \({y_1\geq\ldots\geq y_n}\) ба эерэг тоон \({\lambda_1,\ldots,\lambda_n}\) дарааллууд өгөгдсөн бол 

\(\displaystyle  \begin{array}{rcl}  \lambda_1x_1&\leq&\lambda_1y_1,\\ \lambda_1x_1+\lambda_2x_2&\leq&\lambda_1y_1+\lambda_2y_2,\\ \ldots&&\ldots\\ \lambda_1x_1+\ldots+\lambda_{n-1}x_{n-1}&\leq&\lambda_1y_1+\ldots+\lambda_{n-1}y_{n-1},\\ \lambda_1x_1+\ldots+\lambda_nx_{n}&=&\lambda_1y_1+\ldots+\lambda_ny_{n}, \end{array}\)

 байх зайлшгүй бөгөөд хүрэлцээтэй нөхцөл нь дурын бодит \({t}\)-ийн хувьд [

\(\displaystyle  \lambda_1|t-x_1|+\ldots+\lambda_n|t-x_n| \leq \lambda_1|t-y_1|+\ldots+\lambda_n|t-y_n| \ \ \ \ \ (3)\)

] тэнцэл биш биелэх явдал юм. 

Хэрэв бид [(3)](#esymmetric-crit-weight) шинжүүрийн болон Караматын [(2)](#ekaramata-weight) тэнцэл бишийн бүх гишүүдийг тэнцэл бишийн тэмдгийн нэг талд гаргаад бичвэл, дурын бодит \({t}\)-ийн хувьд 

\(\displaystyle  \lambda_1|t-x_1|-\lambda_1|t-y_1|+\ldots+\lambda_n|t-x_n|-\lambda_n|t-y_n| \leq 0\)

 тэнцэл биш биелдэг бол 

\(\displaystyle  \lambda_1f(x_1)-\lambda_1f(y_1)+\ldots+\lambda_nf(x_n)-\lambda_nf(y_n) \leq 0\)

 тэнцэл биш мөн биелнэ гэсэн үр дүнд хүрнэ. Эндээс, \({x_1,\ldots,x_n}\) ба \({y_1,\ldots,y_n}\) гэсэн хоёр цуглуулгын оронд ганцхан цуглуулгатай ажилладаг, дээрхээс илүү ерөнхий тэнцэл биш байдаг юм биш биз гэсэн таамаглал төрнө. Энэ таамаглалын үнэн болохыг Германы математикч Дарий Гринберг [2008 онд](https://arxiv.org/abs/0803.2958) баталсан.

**Теорем 7.**  Хэрэв \({f}\) нь \({[a,b]}\) завсар дээрх гүдгэр функц, \({\mu_1,\ldots,\mu_m}\) нь \({\sum_i\mu_i=0}\) байх бодит тоонууд, \({x\in[a,b]^m}\) бөгөөд дурын бодит \({t}\)-ийн хувьд 

\(\displaystyle  \mu_1|t-x_1|+\ldots+\mu_m|t-x_m| \leq0 \ \ \ \ \ (4)\)

 байдаг бол 

\(\displaystyle  \mu_1f(x_1)+\ldots+\mu_mf(x_m) \leq0 \ \ \ \ \ (5)\)

 тэнцэл биш биелнэ. 

##  Баталгаа 

Энэ хэсэгт бид «жинтэй» Караматын тэнцэл бишийг (Теорем 4) батална. Юуны түрүүнд, хэрэв ямар нэг \({k}\) индексийн хувьд \({x_k=y_k}\) бол теоремын томъёоллоос \({x_k}\), \({y_k}\) орсон бүх илэрхийллийг бүрмөсөн хасч болох тул бүх \({k}\)-ийн хувьд \({x_k\neq y_k}\) гэж үзэж болно. Ингээд [(2)](#ekaramata-weight) тэнцэл бишийнхээ зүүн баруун гар талуудын ялгаврыг 

\(\displaystyle  \sum_{k=1}^n \lambda_k[f(x_k)-f(y_k)] = \sum_{k=1}^n (x_k-y_k)\lambda_k\cdot\frac{f(x_k)-f(y_k)}{x_k-y_k} = \sum_{k=1}^n (L_k-L_{k-1})D_k\)

 хэлбэртэй бичье. Бид 

\(\displaystyle  L_k = (x_1-y_1)\lambda_1 + \ldots + (x_k-y_k)\lambda_k = \sum_{i=1}^k\lambda_ix_i - \sum_{i=1}^k\lambda_iy_i\)

 ба 

\(\displaystyle  D_k = \frac{f(x_k)-f(y_k)}{x_k-y_k}\)

 гэсэн тэмдэглэгээнүүд оруулсан. Теоремын нөхцлөөс \({L_k\leq0}\) ба \({L_n=0}\) байгааг ажиглаарай. Одоо [Абелийн нийлбэрийн томъёог](/blog/2018/05/20/abel-summation/) ашиглавал дээрх илэрхийлэл [

\(\displaystyle  \sum_{k=1}^n (L_k-L_{k-1})D_k = \sum_{k=1}^{n-1} L_k(D_{k}-D_{k+1}) + L_nD_n \ \ \ \ \ (6)\)

] болох тул, баталгааг гүйцээхийн тулд 

\(\displaystyle  D_k - D_{k+1} = \frac{f(x_k)-f(y_k)}{x_k-y_k} - \frac{f(x_{k+1})-f(y_{k+1})}{x_{k+1}-y_{k+1}}\)

 хэмжигдэхүүнийг *сөрөг биш* гэж харуулах л үлдлээ.

Үүний тулд, 

\(\displaystyle  \Delta(x,y) = \frac{f(x)-f(y)}{x-y}\)

 хэмжигдэхүүнийг \({x}\), \({y}\) хувьсагч тус бүрийнх нь хувьд үл буурах функц гэж харуулахад хангалттай (Үнэндээ \({\Delta(x,y)=\Delta(y,x)}\) учраас аль нэг хувьсагчийнх нь хувьд л үл буурах функц гээд харуулчихад болно). Учир нь \({D_k=\Delta(x_k,y_k)}\) бөгөөд 

\(\displaystyle  \Delta(x_{k+1},y_{k+1})\leq\Delta(x_k,y_{k+1})\leq\Delta(x_k,y_k),\)

 эсвэл \({x_k=y_{k+1}}\) тохиолдолд шууд 

\(\displaystyle  \Delta(x_{k+1},y_{k+1})\leq\Delta(y_k,y_{k+1})=\Delta(y_k,x_k)=\Delta(x_k,y_k),\)

 болно. Энд \({x_{k+1}\leq x_k=y_{k+1}\leq y_k}\) ба \({y_{k+1}=x_k\neq y_k}\) гэдгийг санаарай.

Тэгэхээр дээр дурдагдсан үл буурах чанарыг харуулах үүднээс \({[a,b]}\) завсарт \({x\(\displaystyle  y= \frac{z-y}{z-x}x + \frac{y-x}{z-x}z\)

 тул, Йенсений тэнцэл биш 

\(\displaystyle  f(y) \leq \frac{z-y}{z-x} f(x) + \frac{y-x}{z-x} f(z)\)

 гэж өгнө. Үүний хоёр талыг \({z-x}\) хоёр гишүүнтээр үржүүлбэл 

\(\displaystyle  (z-x)f(y) = (z-y)f(y) + (y-x)f(y) \leq (z-y) f(x) + (y-x) f(z)\)

 болох ба, одоо үүнийгээ \({(y-x)(z-x)}\) илэрхийлэлд хувааснаар 

\(\displaystyle  \frac{f(y)}{y-x} + \frac{f(y)}{z-y} \leq \frac{f(x)}{y-x} + \frac{f(z)}{z-y}\)

 буюу 

\(\displaystyle  \Delta(x,y)\leq\Delta(z,y)\)

 гэж мөрдөнө. Нөгөө талаас, бид 

\(\displaystyle  y = \frac{z-y}{z-x}x + \big( 1-\frac{z-y}{z-x} \big) z = \big( 1-\frac{y-x}{z-x} \big)x + \frac{y-x}{z-x}z\)

 гэж бас бичиж болох ба эндээс 

\(\displaystyle  f(y) \leq \frac{z-y}{z-x} f(x) + \big( 1-\frac{z-y}{z-x} \big) f(z) = \big( 1-\frac{y-x}{z-x} \big) f(x) + \frac{y-x}{z-x} f(z)\)

 буюу 

\(\displaystyle  \Delta(x,z)\leq\Delta(y,z), \qquad \Delta(x,y)\leq\Delta(x,z)\)

 гэж гарна. Ийнхүү [(2)](#ekaramata-weight) тэнцэл биш батлагдлаа.

Бид анхнаасаа бүх \({k}\)-ийн хувьд \({x_k\neq y_k}\) гэж үзсэн тул, \({\lambda_1x_1<\lambda_1y_1}\) буюу \({L_1<0}\). Хэрэв \({f}\) нь эрс гүдгэр бол \({\Delta}\) нь аль ч хувьсагчийнхаа хувьд эрс өсөх функц учраас [(2)](#ekaramata-weight) тэнцэл бишийн эрс болох нь [(6)](#ekaramata-pf-1) томъёоноос шууд мөрдөнө.

##  Тэгшхэмт шинжүүрийн баталгаа 

Бодит \({x_1\geq\ldots\geq x_n}\), \({y_1\geq\ldots\geq y_n}\) ба эерэг \({\lambda_1,\ldots,\lambda_n}\) дарааллууд өгөгдсөн бөгөөд 

\(\displaystyle  \begin{array}{rcl}  \lambda_1x_1&\leq&\lambda_1y_1,\\ \lambda_1x_1+\lambda_2x_2&\leq&\lambda_1y_1+\lambda_2y_2,\\ \ldots&&\ldots\\ \lambda_1x_1+\ldots+\lambda_{n-1}x_{n-1}&\leq&\lambda_1y_1+\ldots+\lambda_{n-1}y_{n-1},\\ \lambda_1x_1+\ldots+\lambda_nx_{n}&=&\lambda_1y_1+\ldots+\lambda_ny_{n}, \end{array}\)

 бол, Теорем 4 ёсоор ямар ч гүдгэр функц \({f}\)-ийн хувьд 

\(\displaystyle  \lambda_1f(x_1)+\ldots+\lambda_nf(x_n) \leq \lambda_1f(y_1)+\ldots+\lambda_nf(y_n)\)

 тэнцэл биш биелнэ. Тухайлбал, \({t}\) гэсэн бодит парамтетртэй \({f(x)=|x-t|}\) функцийг авч үзвэл [

\(\displaystyle  \lambda_1|t-x_1|+\ldots+\lambda_n|t-x_n| \leq \lambda_1|t-y_1|+\ldots+\lambda_n|t-y_n| \ \ \ \ \ (7)\)

] буюу, [(3)](#esymmetric-crit-weight) тэнцэл биш гарч ирнэ.

Одоо [(7)](#esymmetric-crit-weight-pf-1) тэнцэл бишээс дээрх «өргөтгөсөн хашилтын» нөхцлийг гаргах үлдлээ. Юуны түрүүнд, \({t}\) параметрийг \({t>\max\{x_i,y_i\}}\) байхаар сонгож авбал [(7)](#esymmetric-crit-weight-pf-1) тэнцэл бишээс 

\(\displaystyle  \lambda_1(t-x_1)+\ldots+\lambda_n(t-x_n) \leq \lambda_1(t-y_1)+\ldots+\lambda_n(t-y_n)\)

 буюу 

\(\displaystyle  \lambda_1y_1+\ldots+\lambda_ny_n \leq \lambda_1x_1+\ldots+\lambda_nx_n\)

 гэж мөрдөнө. Харин \({t}\) параметрийг \({t<\min\{x_i,y_i\}}\) байхаар сонгож авбал 

\(\displaystyle  \lambda_1(x_1-t)+\ldots+\lambda_n(x_n-t) \leq \lambda_1(y_1-t)+\ldots+\lambda_n(y_n-t)\)

 буюу 

\(\displaystyle  \lambda_1x_1+\ldots+\lambda_nx_n \leq \lambda_1y_1+\ldots+\lambda_ny_n .\)

 Дүгнэвэл [

\(\displaystyle  \lambda_1x_1+\ldots+\lambda_nx_n = \lambda_1y_1+\ldots+\lambda_ny_n . \ \ \ \ \ (8)\)

] Дараагийн алхам болгоод \({y_2\leq t\leq y_1}\) гэж сонговол [(7)](#esymmetric-crit-weight-pf-1) тэнцэл биш 

\(\displaystyle  \lambda_1|t-x_1|+\ldots+\lambda_n|t-x_n| \leq \lambda_1(y_1-t)+\lambda_2(t-y_2)+\ldots+\lambda_n(t-y_n)\)

 хэлбэрт орох ба зүүн гар талд нь 

\(\displaystyle  x_1-t\leq|t-x_1|,\quad t-x_2\leq|t-x_2|,\quad\ldots,\quad t-x_n\leq|t-x_n|,\quad\)

 тэнцэл бишүүдийг хэрэглэснээр 

\(\displaystyle  \lambda_1x_1-\lambda_2x_2-\ldots-\lambda_nx_n \leq \lambda_1y_1-\lambda_2y_2-\ldots-\lambda_ny_n\)

 болж хувирна. Ингээд [(8)](#ekaramata-sym-crit-pf-2) тэнцэтгэлийг хоёр тал дээр нь нэмбэл 

\(\displaystyle  \lambda_1x_1 \leq \lambda_1y_1\)

 нөхцөл мөрдөнө. Цааш нь, \({t}\) параметрээ \({y_3\leq t\leq y_2}\) байхаар сонгох гэх мэтээр үргэлжлүүлснээр «өргөтгөсөн хашилтын» бүх 

\(\displaystyle  \begin{array}{rcl}  \lambda_1x_1+\lambda_2x_2&\leq&\lambda_1y_1+\lambda_2y_2,\\ \ldots&&\ldots\\ \lambda_1x_1+\ldots+\lambda_{n-1}x_{n-1}&\leq&\lambda_1y_1+\ldots+\lambda_{n-1}y_{n-1},\\ \end{array}\)

 нөхцлүүд амархан гарна.

##  Теорем 2-ын баталгаа 

Теорем 2 буюу «жингүй, цэвэр» Караматын хувьд бол, Теорем 4-ийн \({\lambda_1=\ldots=\lambda_n=1}\) хувилбар \({x\prec y}\) нөхцлөөс гүдгэр функц \({f}\) болгоны хувьд 

\(\displaystyle  f(x_1)+\ldots+f(x_n) \leq f(y_1)+\ldots+f(y_n)\)

 тэнцэл биш мөрдөнө гэж хэлнэ. Урвуугаар, хэрэв энэ тэнцэл биш гүдгэр функц \({f}\) болгоны хувьд биелдэг бол \({f(x)=|x-t|}\) хэлбэрийн бүх функцийн хувьд биелэх нь тодорхой. Иймд тэгшхэмт шалгуурын \({\lambda_1=\ldots=\lambda_n=1}\) хувилбараас шууд \({x\prec y}\) гэж гарна. Теорем 2 батлагдлаа.

 

##  Жишээнүүд 

**Жишээ 8.**  Хэрэв \({a,b,c}\) нь гурвалжны талуудын уртууд бол 

\(\displaystyle  \sqrt{a+b-c} + \sqrt{b+c-a} + \sqrt{c+a-b} \leq \sqrt{a} + \sqrt{b} + \sqrt{c}\)

 тэнцэл биш биелэхийг батал. 

*Бодолт.*  Юуны түрүүнд, \({a,b,c}\) нь гурвалжны талуудын уртууд гэдгээс язгуур дорх илэрхийллүүд сөрөг биш. Тэнцэл биш маань \({a,b,c}\) хувьсагчдын хувьд тэгшхэатэй тул \({a\geq b\geq c}\) гэж үзэж болно. Одоо 

\(\displaystyle  a+b-c \geq a, \qquad a+b-c+(c+a-b) = 2a \geq a+b\)

 ба 

\(\displaystyle  a+b-c+(c+a-b)+(b+c-a) = a+b+c\)

 гэдгээс \({(a,b,c)\prec(a+b-c,c+a-b,b+c-a)}\) гэдэг нь илрэх ба Караматын тэнцэл бишийг \({f(x)=\sqrt{x}}\) гэсэн хотгор функц дээр хэрэглэснээр бодлого бодогдоно. \(\Box\)

**Жишээ 9.**  Дурын эерэг \({a,b,c}\) тоонуудын хувьд 

\(\displaystyle  \frac9{a+b+c} \leq \frac2{a+b} + \frac2{b+c} + \frac2{c+a} \leq \frac1a + \frac1b + \frac1c\)

 гэж харуул. 

*Бодолт.*  Тэнцэл биш маань \({a,b,c}\) хувьсагчдын хувьд тэгшхэмтэй тул \({a\geq b\geq c}\) гэж үзэж болно. Одоо 

\(\displaystyle  \frac{a+b}2 \leq a, \qquad \frac{a+b}2+\frac{a+c}2 = a+\frac{b+c}2 \leq a+b\)

 ба 

\(\displaystyle  \frac{a+b}2+\frac{a+c}2+\frac{b+c}2 = a+b+c\)

 гэдгээс \({(\frac{a+b}2,\frac{a+c}2,\frac{b+c}2)\prec(a,b,c)}\). Ингээд Караматыг \({f(x)=\frac1x}\) гэсэн гүдгэр функцийн хувьд хэрэглэснээр 

\(\displaystyle  \frac1a+\frac1b+\frac1c \geq \frac1{\frac{a+b}2} + \frac1{\frac{a+c}2} + \frac1{\frac{b+c}2} = \frac2{a+b} + \frac2{a+c} + \frac2{b+c} .\)

 Цаашилбал, 

\(\displaystyle  \frac{a+b+c}3 \leq \frac{a+b}2, \qquad \frac{a+b+c}3+\frac{a+b+c}3 \leq \frac{a+b}2+\frac{a+c}2\)

 гэдгээс \({(\frac{a+b+c}3,\frac{a+b+c}3,\frac{a+b+c}3)\prec(\frac{a+b}2,\frac{a+c}2,\frac{b+c}2)}\) гарах ба, Караматыг дахин хэрэглэснээр 

\(\displaystyle  \frac1{\frac{a+b}2} + \frac1{\frac{a+c}2} + \frac1{\frac{b+c}2} \geq \frac3{\frac{a+b+c}3} = \frac9{a+b+c}\)

 болж, бодлого бодогдоно. \(\Box\)

 [![](/blog/assets/wp-media/2021/01/karamata_jovan.jpg)](/blog/assets/wp-media/2021/01/karamata_jovan.jpg)Йован Карамата (1902–1967).
