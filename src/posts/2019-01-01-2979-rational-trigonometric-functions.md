---
layout: "layouts/post.njk"
title: "Рационал тригонометрийн функцүүд"
date: "2019-01-01T20:44:28"
slug: "rational-trigonometric-functions"
permalink: "/2019/01/01/rational-trigonometric-functions/"
wordpress_id: 2979
wordpress_url: "https://t8m8r.wordpress.com/2019/01/01/rational-trigonometric-functions/"
categories: ["Анализ"]
tags: ["интеграл", "стереограф проекцлол", "стереографик проекцлол", "тригонометр", "эх функц"]
status: "publish"
comments_count: 0
math: true
generated_by: "wordpress-importer"
templateEngineOverride: "md"
---

\(R(u,v)\) нь 2 хувьсагчийн рационал функц байг. Тодруулбал, \(P(u,v)\) ба \(Q(u,v)\) гэсэн 2 хувьсагчийн олон гишүүнтүүдийн хувьд

\(\displaystyle R(u,v)=\frac{P(u,v)}{Q(u,v)}\)

байг. Тэгвэл \(R(\sin x,\cos x)\) илэрхийллийг *рационал тригонометрийн функц* гэж нэрлэдэг. Ийм функцийн интеграл

\(\displaystyle \int R(\sin x,\cos x)dx\)

нь рационал функцийн интегралд

\(x=2\arctan t\)

гэсэн орлуулгаар шилждэг. Үнэндээ

\(\displaystyle \sin x=\frac{2t}{1+t^2},\qquad \cos x=\frac{1-t^2}{1+t^2},\qquad dx=\frac{2dt}{1+t^2}\qquad(*)\)

болохыг хялбархан шалгаж болно. Тэгэхээр

\(\displaystyle \int R(\sin x,\cos x)dx=2\int R\Big(\frac{2t}{1+t^2},\frac{1-t^2}{1+t^2}\Big)\frac{dt}{1+t^2}.\)

Энэ орлуулгыг [1766 он гэхэд](http://eulerarchive.maa.org/pages/E342.html) Эйлер мэдэж байсан байгаа.

[![](/blog/assets/wp-media/2019/01/screenshot-2019-01-07-15.55.20.png)](/blog/assets/wp-media/2019/01/screenshot-2019-01-07-15.55.20.png) Эйлерийн «Institutionum calculi integralis» 1768. 148-р тал

Рационал тригонометрийн функц \(R(\sin x,\cos x)\)-ийг \(u^2+v^2=1\) гэсэн нэгж тойрог дээр тодорхойлогдсон функц гэж үзвэл, \((*)\) орлуулга нь дараах зурагт дүрслэгдсэн стереографик проекцлол болно.

[![](/blog/assets/wp-media/2019/01/ster.png)](/blog/assets/wp-media/2019/01/ster.png)

Гурвалжны төсөөнөөс

\(u=(1+v)t\)

гэж гарах ба үүнийг \(u^2+v^2=1\) тэгшитгэлтэй хамтатган, \(u,v\) координатуудыг олбол

\(\displaystyle 1-v^2=(1+v)^2t^2\qquad\Longrightarrow\qquad v=\frac{1-t^2}{1+t^2},\qquad u=\frac{2t}{1+t^2}.\)

Иймд \((*)\) орлуулга нь тойргийг *рационал* функцээр параметрчилсэн параметрчлэл юм.

[![](/blog/assets/wp-media/2019/01/eusub.png)](/blog/assets/wp-media/2019/01/eusub.png) (*) орлуулгаар *t* = ±∞ цэгүүд *x* = ±π цэгүүдэд харгалзана.

Дээрх орлуулга нь бүх тохиолдолд ажиллах ерөнхий арга. Тухайн тохиолдлуудад тусгай орлуулгууд илүү тохиромжтой байж мэднэ. Жишээлбэл, \(s=\sin x\) буюу

\(\displaystyle  x=\arcsin s,\qquad dx=\frac{ds}{\sqrt{1-s^2}}\)

орлуулгыг авч үзье. Энэ орлуулгаар

\(\displaystyle \int R(\sin x,\cos x)dx=\int\frac{R(s,\sqrt{1-s^2})ds}{\sqrt{1-s^2}}=\int\frac{P(s,\sqrt{1-s^2})ds}{Q(s,\sqrt{1-s^2})\sqrt{1-s^2}}\)

болно. Хэрэв \(P(u,v)\) нь \(v\) хувьсагчийнхаа зөвхөн *тэгш* зэргүүдийг агуулсан, \(Q(u,v)\) нь \(v\) хувьсагчийнхаа зөвхөн *сондгой* зэргүүдийг агуулсан бол, дээрх интегралын дорх илэрхийлэл язгуураас чөлөөлөгдөж, \(s\)-ийн хувьд рационал функцэд шилжих нь тодорхой. Үүнтэй төстэйгөөр, \(P(u,v)\) ба \(Q(u,v)\) олон гишүүнтүүдийн тэгш сондгойг сольсон нөхцөлд бас болно.

**Жишээ.** \(R(u,v)=\frac{u^3v-uv^2}{u^4v^3+v+u^2}\) үед

\(\displaystyle \int \frac{\cos^3x\sin x-\cos x\sin^2x}{\cos^4x\sin^3x+\sin x+\cos^2x}dx=\int\frac{(1-s^2)s-s^2}{(1-s^2)^2s^3+s+(1-s^2)}ds.\)

**Дасгал.** \(t=\cos x\) орлуулга ямар үед тохиромжтой болохыг судал.

[![](/blog/assets/wp-media/2019/01/Jakob_Bernoulli.jpg)](/blog/assets/wp-media/2019/01/Jakob_Bernoulli.jpg) Интеграл-дифференциал тооллыг үндэслэгчдийн нэг Якоб Бернулли (1655–1705)
