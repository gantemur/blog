---
layout: "layouts/post.njk"
title: "Бернуллийн тэнцэл биш"
date: "2018-12-24T21:30:02"
slug: "bernoulli-inequality"
permalink: "/2018/12/24/bernoulli-inequality/"
wordpress_id: 2954
wordpress_url: "https://t8m8r.wordpress.com/2018/12/24/bernoulli-inequality/"
categories: ["Анализ", "Тэнцэл биш"]
tags: ["Бернулли", "де Слюз"]
status: "publish"
comments_count: 1
math: true
generated_by: "wordpress-importer"
templateEngineOverride: "md"
---

Алдарт Бернуллийн тэнцэл биш нь \(\alpha\geq1\) ба \(x\geq-1\) үед биелдэг

\((1+x)^\alpha\geq 1+\alpha x\)

хэлбэрийн тэнцэл биш байгаа. Үүнд \(\alpha=1\) эсвэл \(x=0\) биш л бол Бернуллийн тэнцэл биш нь *эрс* тэнцэл биш болно.

[![](/blog/assets/wp-media/2018/12/bernoulli.png)](/blog/assets/wp-media/2018/12/bernoulli.png)

Энэ тэнцэл бишийг [Якоб Бернулли](http://www-history.mcs.st-andrews.ac.uk/Biographies/Bernoulli_Jacob.html) 1689 онд [хэвлүүлсэн номондоо](https://archive.org/stream/jacobibernoulli00conggoog#page/n494) оруулснаас үүдэн  бид Бернуллийн тэнцэл биш гэж нэрлэдэг. Гэвч үнэндээ Бернуллийг 13 настай байхад Бельгийн математикч [Рене-Франсуа де Слюз](http://www-history.mcs.st-andrews.ac.uk/Biographies/Sluze.html) энэ тэнцэл бишийг [хэвлүүлж байжээ](https://books.google.com/books?id=ugJ1GtyH08kC&pg=PA114).

[gallery type="rectangular" columns="2" link="file" size="medium" ids="2957,2956"]

Слюзийн номыг нь унших гэж оролдоод барсангүй. Харин Бернуллийн номны холбогдох хэсгийг Google Translate руу хийж байгаад харахад иймэрхүү маягаар томъёолсон байна:

> A, B, C, D, E, ... гэсэн геометр прогресс, A, B, F, G, H, ... гэсэн арифметик прогресс өгөгдсөн ба A, B гэсэн хоёр тоогоор хоёулаа гараагаа эхэлдэг бол, геометр прогрессын үлдсэн гишүүд нь арифметик прогрессынхоо харгалзах гишүүдээс их, гуравдахь гишүүн нь гуравдахь гишүүнээсээ, дөрөвдэх нь дөрөвдэхээсээ, сүүлчийнх нь сүүлчийнхээсээ, гэх мэтчилэн.

Латин эх нь:

[![](/blog/assets/wp-media/2018/12/Screenshot-2018-12-24-22.19.53.png)](/blog/assets/wp-media/2018/12/Screenshot-2018-12-24-22.19.53.png) J. Bernoulli. Positiones Arithmeticae de Seriebus Infinitis (Basel, 1689). 380-р тал.

Бернуллийн тэнцэл бишийг \(\alpha\in\mathbb{N}\) үед [индукцээр батлахад](https://en.wikipedia.org/wiki/Bernoulli%27s_inequality) амархан. Ерөнхий тохиолдолд бол уламжлал оролцуулсан шинжүүр хэрэглэж болно. Энд логарифм функцийн чанарыг ашигласан нэгэн хялбар баталгааг толилуулъя. Юуны түрүүнд, логарифмын хотгор чанараас

\(\displaystyle
\frac1\alpha\log(1+x)
=\frac{\alpha-1}\alpha\log1+\frac1\alpha\log(1+x)
\leq\log\big(\frac{\alpha-1}\alpha+\frac{1+x}\alpha\big)
=\log\big(1+\frac{x}\alpha\big)\)

гэж гарна. Үүнд \(\alpha\neq1\) ба \(x\neq0\) бол тэнцэтгэл биш эрс байна гэдгийг анхаар. Мөн илэрхийлэлд орсон логарифмын утгууд тодорхойлогдож байхын тулд \(x>-1\), хотгор чанарын тэнцэл биш биелдэг байхын тулд \(\alpha\geq1\) байх хэрэгтэй. Одоо логарифмын өсөх чанараас \((1+x)^{\frac1\alpha}
\leq1+\frac{x}\alpha\) буюу

\(\displaystyle
1+x
\leq\big(1+\frac{x}\alpha\big)^{\alpha}\)

гэж гарах ба, эндээс \(\frac{x}\alpha\mapsto x\) гэсэн орлуулгаар

\(\displaystyle
1+\alpha x
\leq(1+x)^{\alpha}\)

болно. Энэ гаргалгаанд шаардагдсан нөхцлүүдийг дахин дүгнэвэл: \(\alpha\geq1\) ба \(x>-\frac1\alpha\).

**Дасгал.** Дээрх аргыг ашиглан \(0\leq\alpha\leq1\) ба \(x\geq-1\) үед

\((1+x)^\alpha\leq 1+\alpha x\)

байна гэж батал. Эрс тэнцэл биш нь ямар үед биелэх вэ?
