---
layout: "layouts/post.njk"
title: "Эйлерийн нийлбэрийн хууль"
date: "2019-01-05T04:19:11"
slug: "euler-law-of-addition"
permalink: "/2019/01/05/euler-law-of-addition/"
wordpress_id: 3038
wordpress_url: "https://t8m8r.wordpress.com/2019/01/05/euler-law-of-addition/"
categories: ["Анализ"]
tags: ["Эйлер", "лемнискат", "нийлбэрийн хууль", "эллипслэг интеграл"]
status: "publish"
comments_count: 0
math: true
generated_by: "wordpress-importer"
templateEngineOverride: "md"
---

Давхар өнцгийн синусын

\(\displaystyle2\int_0^{x}\frac{dt}{\sqrt{1-t^2}}=\int\displaylimits_0^{2x\sqrt{1-x^2}}\frac{dt}{\sqrt{1-t^2}}\)

томъёотой төстэй

\(\displaystyle2\int_0^{x}\frac{dt}{\sqrt{1-t^4}}=\int\displaylimits_0^{2x\sqrt{1-x^4}/(1+x^4)}\frac{dt}{\sqrt{1-t^2}}\)

томъёог Италийн математикч Жюлио Фаньяно 1715 оны үед олсон тухай бид [өмнө дурдсан](/blog/2019/01/04/fagnano-doubling-formula/). Түүний энэ үр дүн олны анхааралд хүрэлгүй байсаар 1750-аад онтой золгож, Фаньяно нас өндөр болсон тул өөрийн нэг насны ажлаа Берлиний академи руу явуулсныг нь 1750 оны 12 сарын 23-нд Эйлер хүлээж авчээ. Фаньяногийн үр дүн Эйлерийн сонирхлыг маш ихээр татаж, Фаньяно ч амьд байхдаа өөрийн ажлыг их багшид өндрөөр үнэлүүлж амжсан байна. Энэ өдрийг сүүлд [Карл Якоби](https://en.wikipedia.org/wiki/Carl_Gustav_Jacob_Jacobi) «эллипслэг функцийн төрсөн өдөр» гэж нэрлэсэн.

Давхар өнцгийн томъёог бодвол илүү ерөнхий

\(\sin(\alpha+\beta)=\sin\alpha\cos\beta+\sin\beta\cos\alpha=\sin\alpha\sqrt{1-\sin^2\beta}+\sin\beta\sqrt{1-\sin^2\alpha}\)

гэсэн нийлбэрийн томъёо байдаг. Үүнийг арксинусын хувьд

\(\arcsin x+\arcsin y=x\sqrt{1-y^2}+y\sqrt{1-x^2}\)

гэж бичсэнээр тойргийн интеграл хэлбэр нь

\(\displaystyle\int_0^{x}\frac{dt}{\sqrt{1-t^2}}+\int_0^{y}\frac{dt}{\sqrt{1-t^2}}=\int\displaylimits_0^{x\sqrt{1-y^2}+y\sqrt{1-x^2}}\frac{dt}{\sqrt{1-t^2}}\)

олдоно. Давхар өнцгийн томъёо нь мэдээж үүний \(x=y\) байх тухайн тохиолдол нь болно. Лемнискатын хувьд төдийгүй илүү ерөнхий эллипслэг интегралуудын хувьд ийм нийлбэрийн томъёог 1753 онд Эйлер олсон юм.

Фаньяно томъёогоо гаргахдаа

\(\displaystyle x=\frac{2y\sqrt{1-y^4}}{1+y^4}\qquad(*)\)

хувиргалтаар

\(\displaystyle \int\frac{dx}{\sqrt{1-x^4}}=2\int \frac{dy}{\sqrt{1-y^4}}\)

болдгийг ажигласан байгаа (Фаньяногийн томъёо нь энэ тэнцэтгэлийг тодорхой интеграл болгосон хэлбэр нь л юм). Тодруулбал, \((*)\) хувиргалтаар

\(\displaystyle dx=\frac{2(y^8-6y^4+1)dy}{(1+y^4)^2\sqrt{1-y^4}},\qquad1-x^4=\frac{(y^8-6y^4+1)^2}{(1+y^4)^4}\)

гэдгийг тооцож болох ба

\(\displaystyle \frac{dx}{\sqrt{1-x^4}}=2\frac{dy}{\sqrt{1-y^4}}.\qquad(**)\)

Эйлер үүнийг \(x=x(y)\) функцийн хувьд дифференциал тэгшитгэл гэж үзсэн. Өөрөөр хэлбэл \((*)\) томъёогоор өгөгдсөн \(x=x(y)\) функц нь

\(\displaystyle \frac{dx}{dy}=2\sqrt{\frac{1-x^4}{1-y^4}}\)

дифференциал тэгшитгэлийн шийд болно.

Ингээд Эйлерт \((**)\) тэгшитгэлийн оронд илүү хялбар

\(\displaystyle \frac{dx}{\sqrt{1-x^4}}=\frac{dy}{\sqrt{1-y^4}}.\qquad(\dagger)\)

тэгшитгэлийг судлах санаа төржээ. Жирийн үед ийм тэгшитгэлийн хоёр талыг шууд тус тусад нь интегралчлаад бодчихдог. Гэхдээ энэ тэгшитгэлийг тэгж интегралчлах элементар функц байхгүй.  Тэгэхээр өөр аргаар үзэх хэрэгтэй. Эйлер юуны түрүүнд

\(\displaystyle x=y,\qquad x=-\sqrt{\frac{1-y^2}{1+y^2}}\)

гэсэн хоёр хялбар шийдийг анзаарсан. Эхний \(x=y\) хувиргалт бол тривиал шийд болох нь ойлгомжтой. Хоёрдахь хувиргалтын хувьд

\(\displaystyle dx=\frac{2ydy}{(1+y^2)\sqrt{1-y^4}},\qquad 1-x^4=\frac{4y^2}{(1+y^2)^2}\)

тул мөн шийд болно гэдгийг хялбархан шалгаж болно. Дээрх хоёр хувиргалтыг язгуураас чөлөөлөн, далд функц байдлаар

\(\displaystyle x-y=0,\qquad x^2+y^2+x^2y^2-1=0\)

гэж бичээд, хоёуланг нь багтаасан

\(\displaystyle x^2+y^2-2\beta xy+\gamma x^2y^2-\gamma=0\qquad(\dagger\dagger)\)

тэнцэтгэлийг авч үзье. Энэ тэнцэтгэлийн \(\beta=1,\,\gamma=0\) тохиолдол нь эхний шийдийг, \(\beta=0,\,\gamma=1\) тохиолдол нь хоёрдахь шийдийг өгнө. Одоо \((\dagger)\) тэгшитгэлийг хангах \(\beta\) ба \(\gamma\) параметрүүдийн шинэ утгууд олох гэж оролдъё. Эхлээд \((\dagger\dagger)\) тэнцэтгэлээс дифференциал авбал

\(\displaystyle 2xdx+2ydy-2\beta xdy-2\beta ydx +2\gamma xy^2dx+2\gamma x^2ydy=0\)

буюу

\(\displaystyle (x-\beta y+\gamma xy^2)dx+(y-\beta x+\gamma x^2y)dy=0\qquad(\ddagger)\)

гарна. Нөгөө талаас, \((\dagger\dagger)\) тэнцэтгэлээс \(x\)-ийг олбол

\(\displaystyle x=\frac{\beta y\pm\sqrt{\beta^2y^2+(1+\gamma y^2)(\gamma-y^2)}}{1+\gamma y^2}\)

буюу

\(\displaystyle (1+\gamma y^2)x-\beta y=\pm\sqrt{\beta^2y^2+(1+\gamma y^2)(\gamma-y^2)}.\)

Үүнтэй төстэйгөөр, \((\dagger\dagger)\) тэнцэтгэлээс \(y\)-ийг олох замаар

\(\displaystyle (1+\gamma x^2)y-\beta x=\pm\sqrt{\beta^2x^2+(1+\gamma x^2)(\gamma-x^2)}\)

томъёог гаргаж болно. Сүүлийн хоёр томъёог \((\ddagger)\) тэгшитгэлд орлуулснаар

\(\displaystyle \pm\sqrt{\beta^2y^2+(1+\gamma y^2)(\gamma-y^2)}\,dx\pm\sqrt{\beta^2x^2+(1+\gamma x^2)(\gamma-x^2)}\,dy=0\)

болох ба, \(\pm\) тэмдгүүдээс зохихыг нь сонгоод, хувьсагчдыг ялгавал

\(\displaystyle \frac{dx}{\sqrt{\beta^2x^2+(1+\gamma x^2)(\gamma-x^2)}}=\frac{dy}{\sqrt{\beta^2y^2+(1+\gamma y^2)(\gamma-y^2)}}\qquad(\ddagger\ddagger)\)

хэлбэрт орно. Язгуур дор байгаа илэрхийллүүд нь

\(\displaystyle \beta^2x^2+(1+\gamma x^2)(\gamma-x^2)=\gamma(1-x^4)+(\beta^2+\gamma^2-1)x^2\\\beta^2y^2+(1+\gamma y^2)(\gamma-y^2)=\gamma(1-x^4)+(\beta^2+\gamma^2-1)y^2\)

байгаа. Хэрэв

\(\beta^2+\gamma^2-1=0\)

бол, дээрх илэрхийллүүд харгалзан \(\gamma(1-x^4)\) ба \(\gamma(1-y^4)\) болох ба,

\(\gamma>0\)

нөхцлийг шаардсанаар язгуур гаргах боломжтой болох тул \((\ddagger\ddagger)\) тэгшитгэл

\(\displaystyle \frac{dx}{\sqrt{1-x^4}}=\frac{dy}{\sqrt{1-y^4}}\)

хэлбэрт орж, бодлого маань бодогдоно. Одоо \(\gamma>0\) нөхцлийг автоматаар хангах үүднээс \(\gamma=b^2\) гэж бичвэл

\(\displaystyle \beta=\sqrt{1-\gamma^2}=\sqrt{1-b^4}\)

ба \((\dagger\dagger)\) тэнцэтгэл маань

\(\displaystyle x^2+y^2-2xy\sqrt{1-b^4}+b^2 x^2y^2-b^2=0\qquad(\S)\)

болж хувирна. Энэ параграфыг дүгнэвэл, \(b\) параметрийн ямар ч бодит утганд харгалзах \((\S)\) буюу

\(\displaystyle x=\frac{y\sqrt{1-b^4}+b\sqrt{1-y^4}}{1+b^2y^2}\)

хувиргалт нь

\(\displaystyle \frac{dx}{\sqrt{1-x^4}}=\frac{dy}{\sqrt{1-y^4}}\)

тэнцэтгэлийг хангана.

Дээрх хувиргалтаар \(y=0\) цэг \(x=b\) цэгт хувирч байгаа. Тэгэхээр

\(\displaystyle \int\displaylimits_b^{\frac{y\sqrt{1-b^4}+b\sqrt{1-y^4}}{1+b^2y^2}}\frac{dx}{\sqrt{1-x^4}}=\int_0^y\frac{dy}{\sqrt{1-y^4}}\)

буюу

\(\displaystyle \int_0^y\frac{dt}{\sqrt{1-t^4}}+\int_0^b\frac{dt}{\sqrt{1-t^4}}=\int\displaylimits_0^{\frac{y\sqrt{1-b^4}+b\sqrt{1-y^4}}{1+b^2y^2}}\frac{dt}{\sqrt{1-t^4}}\)

гэсэн үг. Өөрөөр хэлбэл, лемнискатын нумын уртыг

\(\displaystyle L(a)=\int_0^a\frac{dt}{\sqrt{1-t^4}}\)

гэж тэмдэглэвэл

\(\displaystyle L(a)+L(b)=L\Big(\frac{a\sqrt{1-b^4}+b\sqrt{1-a^4}}{1+a^2b^2}\Big)\)

гэсэн нийлбэрийн томъёо гарч ирлээ. Энэ гайхамшигт томъёог Эйлер 1753 онд олж Санкт Петербургийн академид илтгэсэн нь [1761 онд хэвлэгдсэн](http://eulerarchive.maa.org/pages/E251.html). Эйлерийн томъёоны \(a=b\) байх тухайн тохиолдол нь [Фаньяногийн томъёо](/blog/2019/01/04/fagnano-doubling-formula/) болно.

Эйлер мэдээж лемнискатаар хязгаарлагдсангүй,

\(g(x)=1+mx^2+nx^4\)

олон гишүүнт бүхий

\(\displaystyle \int\frac{dx}{\sqrt{g(x)}}\)

хэлбэрийн интегралуудыг бас авч үзсэн (Энд \(m=-k^2-1,\,n=k^2\) гэж авбал нэгдүгээр төрлийн эллипслэг интегралын Лежандр нормаль хэлбэр болно гэдгийг анхаар). Үнэндээ \((\dagger\dagger)\) маягийн хувиргалтанд

\(\beta^2-\gamma^2+1=\gamma m\)

гэж сонгосноор \(g(x)=1-x^4+mx^2\) тохиолдлыг бид шууд хамарч болох байсан. Одоо \((\dagger\dagger)\) хувиргалтын оронд нэг илүү параметртэй

\(\displaystyle x^2+y^2-2\beta xy+\gamma x^2y^2-\delta=0\)

маягийн хувиргалтуудыг авч үзвэл \((\ddagger)\) өөрчлөгдөхгүй хэвээр үлдэх ба \((\ddagger\ddagger)\) томъёо дараах томъёогоор солигдоно:

\(\displaystyle \frac{dx}{\sqrt{\beta^2x^2+(1+\gamma x^2)(\delta-x^2)}}=\frac{dy}{\sqrt{\beta^2y^2+(1+\gamma y^2)(\delta-y^2)}}.\)

Эндээс

\(\gamma=-n\delta,\qquad \beta^2+\gamma\delta-1=m\delta\)

гэсэн тэгшитгэлүүдэд хүрэх бөгөөд, \(\delta=b^2\) гээд хөөвөл

\(\gamma=-nb^2,\qquad \beta^2=1+mb^2+nb^4=g(b)\)

буюу

\(\displaystyle x^2+y^2=b^2(1+nx^2y^2)+2xy\sqrt{g(b)}\)

гэсэн хувиргалт гарна. Өөрөөр хэлбэл

\(\displaystyle x=\frac{y\sqrt{g(b)}+b\sqrt{g(y)}}{1-nb^2y^2}.\)

Үүгээр \(y=0\) цэг бас \(x=b\) цэгт бууж байгаа. Тэгэхээр

\(\displaystyle F(a)=\int_0^a\frac{dt}{\sqrt{g(t)}}\)

гэж тэмдэглэвэл

\(\displaystyle F(a)+F(b)=F\Big(\frac{a\sqrt{g(b)}+b\sqrt{g(a)}}{1-na^2b^2}\Big)\)

гэсэн эллипслэг интегралын нийлбэрийн хууль гарч ирнэ.

Эйлер цааш нь дурын 4 зэргийн олон гишүүнтийг, зарим 6 зэргийн олон гишүүнтийг ч авч үзсэн. Үүнээс хойш [10 гаран жилийн дараа](http://eulerarchive.maa.org/pages/E345.html) Эйлер энэ бодлогонд дахин анхаарлаа хандуулж, дурын 4 зэргийн олон гишүүнтийг \(g(x)=1+mx^2+nx^4\) хэлбэрт шилжүүлдэг бутархай шугаман хувиргалтыг олсноор ерөнхий эллипслэг интегралын нийлбэрийн хуулийг томъёолох системтэй арга бий болсон юм.

**Дасгал.** Эйлерийн аргыг ашиглан \(g(x)=m+nx^3\) хэлбэртэй үед эллипслэг интегралын нийлбэрийн хуулийг гарга.

[![](/blog/assets/wp-media/2019/01/leonard-eiler.jpg)](/blog/assets/wp-media/2019/01/leonard-eiler.jpg)
