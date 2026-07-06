---
layout: "layouts/post.njk"
title: "Бертраны постулат"
date: "2018-05-19T16:21:38"
slug: "bertrand-postulate"
permalink: "/2018/05/19/bertrand-postulate/"
wordpress_id: 244
wordpress_url: "https://t8m8r.wordpress.com/2018/05/19/bertrand-postulate/"
categories: ["Тооны онол", "теорем"]
tags: ["Бертран", "Чебышёв", "анхны тоо"]
status: "publish"
comments_count: 0
math: true
generated_by: "wordpress-importer"
templateEngineOverride: "md"
---

Дараах таамаглалыг Францы математикч Жозеф Бертран 1845 онд дэвшүүлсэн.

> ***Бертраны постулат.** Ямар ч \(n>3\) бүхэл тооны хувьд \(n

Бертран өөрөө энэ таамаглалаа 3 сая хүртэлх анхны тоонуудын хувьд шалгасан боловч баталж чадаагүй. Энэ таамаглалыг

\(\displaystyle n>3\qquad\Longrightarrow\qquad\pi(2n-3)-\pi(n)>0\)

маягаар бас илэрхийлж болно. Яагаад \(n>3\) гэсэн нөхцөл хэрэгтэй нь ойлгомжтой:

\(\pi(2\cdot2-3)-\pi(2)=-1, \qquad\pi(2\cdot3-3)-\pi(3)=0.\)

Дорх зурагт \(f(x)=\pi(2x-3)-\pi(x)\) функцийн графикийг \([2,18]\) мужид үзүүлэв.

[![](/blog/assets/wp-media/2018/05/bertrand2.png)](/blog/assets/wp-media/2018/05/bertrand2.png)

Цааш нь \(x=180\) хүртэл шалгахад ийм байна:

[![](/blog/assets/wp-media/2018/05/bertrand.png)](/blog/assets/wp-media/2018/05/bertrand.png)

Чебышёв \(x\) их үед

\(A\cdot\mathrm{Li}(x)<\pi(x)<\frac65A\cdot\mathrm{Li}(x)\)

гэж харуулсан (\(A=\log\frac{2^{1/2}3^{1/3}5^{1/5}}{30^{1/30}}=0.9212\ldots\)). Эндээс \(x\) их үед

\(\displaystyle\pi(2x-3)-\pi(x)>A\cdot\mathrm{Li}(2x)-\frac65A\cdot\mathrm{Li}(x)\sim\frac25A\cdot\frac{x}{\ln x}\)

маягаар өснө гэж гарна. Тэгэхээр Бертраны постулатыг батлахын тулд энэ зааг \(x\)-ийн ямар утгаас эхэлж биелэхийг тодруулаад, түүнээс бага \(x\)-ийн утгуудад шууд шалгачихад хангалттай. Мэдээж шууд шалгахын тулд \(x\)-ийг хэдэн мянгын дотор (эсвэл ядаж хэдэн саяын дотор) оруулж ирвэл сайн.

Энэ асуудлыг Чебышёв яаж шийдсэнийг авч үзье. Бид

\(\displaystyle\theta(x)=\sum_{p\leq x}\log p\)

функцийн хувьд

\(\theta(x)<\displaystyle\frac65Ax-A\sqrt{x}+\frac5{4\log6}\log^2\!x+\frac52\log x+1\qquad(*)\)

ба

\(\theta(x)>\displaystyle Ax-\frac{12}5A\sqrt{x}-\frac5{8\log6}\log^2\!x-\frac{15}4\log x-1\qquad(**)\)

[заагуудыг баталсан](/blog/2018/05/17/bounds-on-theta/). Үүнд \(A=\log\frac{2^{1/2}3^{1/3}5^{1/5}}{30^{1/30}}=0.9212\ldots\) нь бидний сайн танил тогтмол. Одоо

\(\displaystyle\theta(x)-\theta(y)=\sum_{y
гэдгээс, Бертраны постулатыг

\(\displaystyle n>3\qquad\Longrightarrow\qquad\theta(2n-3)-\theta(n)>0\)

гэж илэрхийлж болно. Дээрх \((*)\) ба \((**)\) заагуудыг ашиглан \(x>y\) үед \(\theta(x)-\theta(y)\) ялгавыг

\(\begin{array}{rcl}\theta(x)-\theta(y)&>&\displaystyle Ax-\frac{12}5A\sqrt{x}-\frac5{8\log6}\log^2\!x-\frac{15}4\log x-1\\&&\displaystyle-\frac65Ay+A\sqrt{y}-\frac5{4\log6}\log^2\!y-\frac52\log y-1\\&>&\displaystyle Ax-\frac65Ay-\frac{12}5A\sqrt{x}-\frac{15}{8\log6}\log^2\!x-\frac{25}4\log x-2\end{array}\)

маягаар доороос нь зааглаж болно. Сүүлийн алхамд \(\sqrt{y}\geq0\) гишүүнийг хаясан ба \(\log y\) агуулсан гишүүдэд \(\log y<\log x\) тэнцэл бишийг хэрэглэсэн. Эндээс хэрэв

\(\displaystyle Ax-\frac65Ay-\frac{12}5A\sqrt{x}-\frac{15}{8\log6}\log^2\!x-\frac{25}4\log x-2\geq0\)

бол, \(\theta(x)-\theta(y)>0\) болох тул, \(y\(\displaystyle y\leq \frac{5x}6-2\sqrt{x}-\frac{25\log^2\!x}{16A\log6}-\frac{125\log x}{24A}-\frac5{3A}\quad\Longrightarrow\quad \theta(y)<\theta(x)\)

буюу,

\(\displaystyle G(x)=\frac{5x}6-2\sqrt{x}-\frac{25\log^2\!x}{16A\log6}-\frac{125\log x}{24A}-\frac5{3A}\qquad(\dagger)\)

функцийг оруулбал

\(y\leq G(x)\quad\Longrightarrow\quad\theta(y)<\theta(x)\quad\Longleftrightarrow\quad\exists p:y
гэсэн үр дүн гарна. Эндээс Бертраны постулатыг батлах жор

\(n\leq G(2n-3)\quad\Longrightarrow\quad\theta(n)<\theta(2n-3)\quad\Longrightarrow\quad\exists p:n
гарч ирнэ. Дорх зурагт \(G(2n-3)\) ба \(f(n)=n\) функцүүдийн \(n\)-ээс хамаарсан графикийг үзүүлэв.

[![](/blog/assets/wp-media/2010/04/berf1-e1526748544421.png)](https://t8m8r.wordpress.com/wp-content/uploads/2010/04/berf1.png)

Зургаас \(n\approx160\) орчмоос эхлээд \(n\leq G(2n-3)\) болж байгаа нь харагдана. Эндээс санаа аваад \(n=160\) дээр \(G(2n-3)\) функцийг тооцож үзвэл

\(G(2\cdot160-3)=162.63\ldots\)

буюу, \(n=160\) үед \(n\leq G(2n-3)\). Энэ тэнцэл биш цаашаа хадгалагдах эсэхийг шалгахын тулд \(F(x)=G(2x-3)-x\) функцийн уламжлалыг бодвол

\(F'(x)=2G'(2x-3)-1\)

болно. Үүнд

\(\displaystyle G'(x)=\frac56-\frac1{\sqrt{x}}-\frac{25}{8A\log6}\cdot\frac{\log x}{x}-\frac{125}{24A}\cdot\frac1x\)

өсөх функц ба \(x\) их үед \(G'(x)\to\frac56\) тул, \(F'(x)\) нь өсөх функц ба \(x\) их үед \(F'(x)\to\frac23\) болох нь тодорхой. Түүнчлэн

\(F'(40)=0.07\ldots\)

гэдгээс, \(x\geq40\) үед \(F'(x)>0\). Өөрөөр хэлбэл \(x\geq40\) үед \(F(x)=G(2x-3)-x\) нь эрс өсөх функц. Тэгэхээр

\(\displaystyle F(n)=G(2n-3)-n\geq0\)

тэнцэл биш \(n\geq160\) үед хүчинтэй нь батлагдана. Харин \(n<160\) үед

\(2,3,5,7,13,23,43,83,163,\)

дараалал дахь зэргэлдээ хоёр (анхны) тооны ялгавар тэр хоёр тооны багаас нь хэтрэхгүй байгааг ажиглахад хангалттай. Үүнтэй давхардуулаад бид дээр \(4\leq n\leq180\) хүртэл шууд шалгасан. Бертраны таамаглал бүрэн батлагдлаа.

[![](/blog/assets/wp-media/2018/05/berfp.png)](/blog/assets/wp-media/2018/05/berfp.png) F'(x) = 2G'(2x–3) – 1 функцийн график

**Тэмдэглэл.** Чебышёвын аргументыг ашиглан \(n\) их үед \(n\frac65\) бодит тооны хувьд харуулах боломжтой. Дорх зурагт жишээ нь \(G(\frac32n)\) функцийн график \(f(n)=n\) шулууныг хаагуур огтолж байгааг дүрслэв.

[![](/blog/assets/wp-media/2010/04/berf32-e1526748582749.png)](https://t8m8r.wordpress.com/wp-content/uploads/2010/04/berf32.png)
