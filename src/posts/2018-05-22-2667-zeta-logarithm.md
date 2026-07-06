---
layout: "layouts/post.njk"
title: "Зета функцийн логарифм ба эх функц"
date: "2018-05-22T19:26:04"
slug: "zeta-logarithm"
permalink: "/2018/05/22/zeta-logarithm/"
wordpress_id: 2667
wordpress_url: "https://t8m8r.wordpress.com/2018/05/22/zeta-logarithm/"
categories: ["Анализ", "Тооны онол"]
tags: ["зета функц"]
status: "publish"
comments_count: 0
math: true
generated_by: "wordpress-importer"
templateEngineOverride: "md"
---

[Өмнөх постоор](/blog/2018/05/22/zeta-pole/) бид \\(s>1\\) үед тодорхойлогдсон

\\(\displaystyle f_1(s)=\zeta(s)-\frac1{s-1}\\)

функцийн бүх зэргийн уламжлал \\(s\to1\\) хязгаарт төгсгөлөг утгатай байна гэдгийг баталсан. Үүнийг

\\(\displaystyle\zeta(s)\sim\frac1{s-1}\qquad(*)\\)

маягаар төсөөлбөл зохимжтой. Нөгөө талаас, Эйлерийн үржвэрийн теоремоос

\\(\displaystyle \ln\zeta(s)=-\sum_p\ln(1-p^{-s})\sim\sum_p\frac1{p^s}\\)

маягийн харьцаа биелнэ гэж бид тааж байгаа (Үүнийг дараагийн постоор жин тан болгоно).

Дээрх хоёр харьцааг хооронд нь холбохын тулд (*) харьцаанаас

\\(\displaystyle\ln\zeta(s)\sim\ln\frac1{s-1}=-\ln(s-1)\\)

гэж таагаад

\\(\displaystyle f_2(s)=\ln\zeta(s)+\ln(s-1)=\ln\big((s-1)\zeta(s)\big)=\ln\big((s-1)f_1(s)+1\big)\\)

функцийн \\(s\to1\\) хязгаарын шинж чанарыг сонирхоё. Юуны өмнө

\\(\displaystyle\lim_{s\to1}f_1(s)\\)

хязгаар төгсгөлөг учир

\\(\displaystyle\lim_{s\to1}f_2(s)=\lim_{s\to1}\ln\big((s-1)f_1(s)+1\big)=\ln1=0\\)

гэж гарна. Цаашилбал

\\(\displaystyle f_2'(s)=\frac{f_1(s)+(s-1)f_1'(s)}{(s-1)f_1(s)+1}\\)

болох ба

\\(N(s)=f_1(s)+(s-1)f_1'(s)\to f_1(1),\qquad D(s)=(s-1)f_1(s)+1\to1\\)

тул \\(f_2'(s)\to f_1(1)\\) байна. Түүнчлэн

\\(\displaystyle f_2''(s)=\frac{N'D-ND'}{D^2},\qquad f_2'''(s)=\frac{(N''D-ND'')D^2-2(N'D-ND')DD'}{D^4}\\)

гэх мэтчилэн явах бөгөөд \\(s\to1\\) үед \\(N(s)\\) ба \\(D(s)\\) функцүүдийн бүх уламжлал төгсгөлөг хязгаартай тул дараах лемм батлагдав.

**Лемм.** \\(s>1\\) үед тодорхойлогдсон

\\(\displaystyle f_2(s)=\ln\zeta(s)-\ln\frac1{s-1}\\)

функцийн бүх зэргийн уламжлал \\(s\to1\\) хязгаарт төгсгөлөг утгатай байна.

[![](/blog/assets/wp-media/2018/05/logzeta.png)](/blog/assets/wp-media/2018/05/logzeta.png)

Одоо \\(\zeta(s)\\) ба \\(\ln\zeta(s)\\) функцүүдийг хооронд нь яаж холбох вэ? Мэдээж \\(\zeta(s)\sim\ln\zeta(s)\\) бол худлаа. Харин

\\(\displaystyle\frac{d}{ds}\ln(s-1)=\frac1{s-1}\\)

гэдгийг санавал,

\\(\displaystyle\zeta(s)\sim\frac1{s-1}=\frac{d}{ds}\ln(s-1)\sim-\frac{d}{ds}\ln\zeta(s)=-\frac{\zeta'(s)}{\zeta(s)}\\)

гарна. Өөрөөр хэлбэл,

\\(\displaystyle f_2'(s)=\frac{d}{ds}\Big(\ln\zeta(s)-\ln\frac1{s-1}\Big)=\frac{\zeta'(s)}{\zeta(s)}+\frac1{s-1}\\)

тул

\\(\displaystyle f_3(s)=\frac{\zeta'(s)}{\zeta(s)}+\zeta(s)=\frac{\zeta'(s)}{\zeta(s)}+\frac1{s-1}+\zeta(s)-\frac1{s-1}=f_2'(s)+f_1(s)\\)

функцийн бүх зэргийн уламжлал \\(s\to1\\) хязгаарт төгсгөлөг утгатай байна.

Дээрх харьцаа «сөрөг зэргийн уламжлал» буюу эх функцүүдийн хувьд бас хүчинтэй. Зета функцийн тодорхойлолтонд \\(n\geq2\\) байх гишүүн тус бүрийг интегралчлаад

\\(\displaystyle Z(s)=-\sum_{n\geq2}\frac1{n^s\ln n}\\)

гэсэн функц тодорхойлбол, \\(Z'(s)=\zeta(s)-1\\) харьцаа биелнэ. Тухайлбал

\\(\displaystyle Z(2)-Z(s)=s-2+\int_s^2\zeta(t)dt\\)

буюу

\\(\displaystyle Z(s)=Z(2)+2-s-\int_s^2\zeta(t)dt.\\)

Үүнтэй төстэйгөөр

\\(\displaystyle \ln\zeta(s)=\ln\zeta(2)-\int_s^2\frac{\zeta'(t)}{\zeta(t)}dt\\)

гэдгээс \\(C=Z(s)+2+\ln\zeta(2)\\) тогтмолтойгоор

\\(\displaystyle Z(s)+\ln\zeta(s)=C-s-\int_s^2\Big(\zeta(t)+\frac{\zeta'(t)}{\zeta(t)}\Big)dt=C-s-\int_s^2f_3(t)dt\\)

гарна. Энд \\(f_3(s)\\) нь \\(s=1\\) дээр төгсгөлөг утгатай, тасралтгүй функц тул \\(s\to1\\) үед

\\(\displaystyle Z(s)+\ln\zeta(s)=C-s-\int_s^2f_3(t)dt\to C-1-\int_1^2f_3(t)dt.\\)

Ингээд дараах теорем батлагдлаа.

**Теорем.** \\(s>1\\) үед тодорхойлогдсон

\\(\displaystyle f_4(s)=Z(s)+\ln\zeta(s)\\)

функцийн бүх зэргийн уламжлал \\(s\to1\\) хязгаарт төгсгөлөг утгатай байна (Бүх зэргийн уламжлал гэдэгт мэдээж 0-р зэргийнх багтана).
