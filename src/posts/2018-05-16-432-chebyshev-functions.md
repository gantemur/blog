---
layout: "layouts/post.njk"
title: "Чебышёвын функцүүд"
date: "2018-05-16T02:14:48"
slug: "chebyshev-functions"
permalink: "/2018/05/16/chebyshev-functions/"
wordpress_id: 432
wordpress_url: "https://t8m8r.wordpress.com/2018/05/16/chebyshev-functions/"
categories: ["Тооны онол"]
tags: ["Мангольдтын функц", "Чебышёвын функц", "анхны тоо"]
status: "publish"
comments_count: 0
math: true
generated_by: "wordpress-importer"
templateEngineOverride: "md"
---

Чебышёв \\(\pi(x)\\) функцийн оронд, \\(x\\)-ээс хэтрэхгүй бүх анхны тоонуудын үржвэрийг \\(\theta(x)\\) гэсэн функцээр дамжуулан судлах санаа дэвшүүлсэн:

\\(\displaystyle\theta(x)=\ln\prod_{p\leq x}p=\sum_{p\leq x}\ln p.\\)

Энэ функцийг \\(\pi(x)\\) функцтэйгээ холбоход амархан. Юуны өмнө

\\(\displaystyle\theta(x)=\sum_{p\leq x}\ln p\leq\sum_{p\leq x}\ln x=\ln x\sum_{p\leq x}1=\pi(x)\ln x.\\)

Цаашилбал, \\(0<\alpha<1\\) ба \\(x>1\\) үед

\\(\begin{array}{rcl}\theta(x)&\geq&\displaystyle\sum_{x^\alpha
Өөрөөр хэлбэл

\\(\displaystyle\theta(x)\leq\pi(x)\ln x\leq\frac{\theta(x)}\alpha+x^\alpha\ln x.\qquad\qquad(*)\\)

Энэ \\(\theta(x)\\) функц нь жирийн факториалтай нягт холбоотой байдгаараа давуу талтай. Факториалаас логарифм аваад

\\(\displaystyle T(x)=\ln([x]!)=\ln\prod_{n\leq x}n=\sum_{n\leq x}\ln n\\)

гэж тэмдэглэе. [Арифметикийн үндсэн теоремоос](/blog/2010/04/21/fundamental-theorem-arithmetics/) дурын натурал тоог

\\(\displaystyle n=\prod_{m\geq1}\prod_{p^m|n}p\qquad\qquad(**)\\)

байдлаар задалж болох ба үүнийг дээрх илэрхийлэлд орлуулбал

\\(\displaystyle T(x)=\sum_{m\geq1}\sum_{n\leq x}\sum_{p^m|n}\ln p=\sum_{m\geq1}\sum_{k\geq1}\sum_{kp^m\leq x}\ln p\\)

болно. Энд \\(p^m\\) тоонд хуваагддаг тоонууд \\(kp^m\\) хэлбэртэй гэдгийг ашигласан. Түүнчлэн, энд оролцож байгаа бүх нийлбэр төгсгөлөг нийлбэр байгааг ажиглаарай. Одоо дээрх нийлбэрийн \\(kp^m\leq x\\) нөхцлийг \\(p\leq\sqrt[m]{\frac{x}k}\\) гэж бичсэнээр бид дараах адилтгалыг гаргаж авна:

\\(\displaystyle T(x)=\sum_{m\geq1}\sum_{k\geq1}\sum_{p\leq\sqrt[m]{\frac{x}k}}\ln p=\sum_{k\geq1}\sum_{m\geq1}\theta\big(\!\!\textstyle\sqrt[m]{\frac{x}k}\,\big).\\)

Жирийн факториалын логарифм болох \\(T(x)\\) ба анхны тоонуудын тархалттай холбоотой \\(\theta(x)\\) функцүүдийг хооронд нь холбож байдгаараа энэ адилтгал Чебышёвын онолын тулгуур нь болж өгдөг. Одоо

\\(\displaystyle \psi(x)=\sum_{m\geq1}\theta\big(\!\!\sqrt[m]{x}\,\big)=\displaystyle\sum_{m\geq1}\sum_{p\leq\sqrt[m]{x}}\ln p=\sum_{m\geq1}\sum_{p^m\leq x}\ln p\\)

гэсэн шинэ функц тодорхойлоод

\\(\displaystyle {T(x)=\sum_{k\geq1}\psi\Big({\frac{x}k}\Big)}\qquad\qquad(\dagger)\\)

байдлаар арай хялбарчилж бичиж болно. Энэ шинэ функцийн тодорхойлолтыг ихэнхдээ шууд

\\(\displaystyle \psi(x)=\sum_{p^m\leq x}\ln p\\)

гэж бичдэг. Үүнд \\({}p^m\leq x\\) байдаг бүх анхны тоо \\(p\\) ба эерэг бүхэл тоо \\(m\\)-ээр нийлбэрийг авна гэсэн үг. Мөн

\\(\displaystyle {}\qquad e^{\psi(x)}=\prod_{p^m\leq x}p=\mathrm{lcd}\{n:n\leq x\}\\)

буюу \\(e^{\psi(x)}\\) нь \\(x\\) хүртэлх бүх бүхэл тооны хамгийн бага ерөнхий хуваагдагч болохыг ажиглаж болно.

Эхний тодорхойлолтоос

\\(\displaystyle \psi(x)=\theta(x)+\theta\big(\!\sqrt{x}\,\big)+\theta\big(\!\sqrt[3]{x}\,\big)+\ldots\geq\theta(x)\\)

гэж гарна. Нөгөө талаас, ямар ч \\(p\\) тооны хувьд \\(p^m\leq x\\) байх хамгийн өндөр зэрэг нь \\(m=\big[\frac{\ln x}{\ln p}\big]\\) тул

\\(\displaystyle \psi(x)=\sum_{p^m\leq x}\ln p=\sum_{p\leq x}\Big[\frac{\ln x}{\ln p}\Big]\ln p\leq\sum_{p\leq x}\frac{\ln x}{\ln p}\ln p=\ln x\sum_{p\leq x}1=\pi(x)\ln x.\\)

Үүнийг дээрх \\((*)\\) томъёотой нийлүүлбэл

\\(\displaystyle\theta(x)\leq\psi(x)\leq\pi(x)\ln x\leq\frac{\theta(x)}\alpha+x^\alpha\ln x.\\)

Өөрөөр хэлбэл бид шууд \\(\psi(x)\\) функцийг судалсан ч болохоор боллоо.

[![](/blog/assets/wp-media/2018/05/psitheta3.png)](/blog/assets/wp-media/2018/05/psitheta3.png)

Хэрэв [Гаусс-Лежандрын таамаглал](/blog/2018/05/15/pnt/) үнэн бол

\\(\displaystyle\limsup_{x\to\infty}\frac{\theta(x)}x\leq\lim_{x\to\infty}\frac{\pi(x)\ln x}x=1\\)

ба \\(\alpha<1\\) тул

\\(\displaystyle1=\lim_{x\to\infty}\frac{\pi(x)\ln x}x\leq\liminf_{x\to\infty}\Big(\frac{\theta(x)}{\alpha x}+\frac{\ln x}{x^{1-\alpha}}\Big)=\frac1\alpha\liminf_{x\to\infty}\frac{\theta(x)}{x}\\)

буюу

\\(\displaystyle\liminf_{x\to\infty}\frac{\theta(x)}{x}\geq\alpha.\\)

Ингээд \\(\alpha<1\\) нь дурын бодит тоо гэдгээс

\\(\displaystyle\lim_{x\to\infty}\frac{\theta(x)}{x}=1.\\)

Одоо \\(x\to\infty\\) үед \\(\frac{\theta(x)}{x}\to1\\) гэж үзвэл

\\(\displaystyle1=\lim_{x\to\infty}\frac{\theta(x)}x\leq\liminf_{x\to\infty}\frac{\psi(x)}x\leq\limsup_{x\to\infty}\frac{\psi(x)}x\leq\lim_{x\to\infty}\Big(\frac{\theta(x)}{\alpha x}+\frac{\ln x}{x^{1-\alpha}}\Big)=\frac1\alpha\\)

болох ба, мөн л \\(\alpha<1\\) нь дурын бодит тоо гэдгээс

\\(\displaystyle\lim_{x\to\infty}\frac{\psi(x)}x=1\\)

гэж мөрдөнө. Үүнтэй төстэйгөөр, \\(x\to\infty\\) үед \\(\frac{\psi(x)}{x}\to1\\) гэдгээс

\\(\displaystyle\lim_{x\to\infty}\frac{\pi(x)\ln x}x=1\\)

гэж харуулахад амархан. Эндээс дүгнэвэл, бид Гаусс-Лежандрын таамаглалын

\\(\displaystyle\lim_{x\to\infty}\frac{\pi(x)\ln x}x=1\quad\Leftrightarrow\quad\lim_{x\to\infty}\frac{\theta(x)}x=1\quad\Leftrightarrow\quad\lim_{x\to\infty}\frac{\psi(x)}x=1\\)

гэсэн эквивалент хэлбэрүүдийг гарган авлаа.

Эцэст нь, дээрх аргументийг арай өөр өнцгөөс харах үүднээс бас нэг шинэ функц тодорхойлъё. Эхлээд \\((**)\\) томъёоноос логарифм авбал

\\(\displaystyle\ln n=\sum_{m\geq1}\sum_{p^m|n}\ln p\\)

гарах бөгөөд баруун гар талд нь \\(n\\) тооны \\(p^m\\) хэлбэрийн хуваагч бүрийн хувьд \\(\ln p\\) нэмэгдэхүүн орж ирж байгаа. Тэгэхээр \\(d=p^m\\) үед \\(\Lambda(d)=\ln p\\) байдаг, \\(d\neq p^m\\) үед \\(\Lambda(d)=0\\) байдаг \\(\Lambda(d)\\) гэсэн функц тодорхойлбол

\\(\displaystyle\ln n=\sum_{m\geq1}\sum_{p^m|n}\ln p=\sum_{d|n}\Lambda(d)\\)

болно. Үүнийг *Мангольдтын функц* гэж нэрлэдэг. Тодорхойлолтыг нь дахин бичвэл

\\(\displaystyle\Lambda(n)=\begin{cases}\ln p&\textrm{if}\quad n=p^m\\0&\textrm{otherwise}\end{cases}\\)

Мангольдтын функцийн тусламжтайгаар \\(\psi(x)\\) функц нь

\\(\displaystyle \psi(x)=\sum_{p^m\leq x}\ln p=\sum_{n\leq x}\Lambda(n)\\)

гэж бичигдэнэ. Үндсэн адилтгалыг бас амархан гаргаж болно. Юун түрүүнд

\\(\displaystyle T(x)=\sum_{n\leq x}\ln n=\sum_{n\leq x}\sum_{d|n}\Lambda(d)=\sum_{k\geq1}\sum_{kd\leq x}\Lambda(d).\\)

Энд \\(d\\) тоонд хуваагддаг тоонууд \\(kd\\) хэлбэртэй гэдгийг ашигласан. Ингээд цаашаа

\\(\displaystyle T(x)=\sum_{k\geq1}\sum_{kd\leq x}\Lambda(d)=\sum_{k\geq1}\sum_{d\leq x/k}\Lambda(d)=\sum_{k\geq1}\psi(x/k)\\)

болж үндсэн адилтгал батлагдана.
