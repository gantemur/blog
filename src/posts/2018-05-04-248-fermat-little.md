---
layout: "layouts/post.njk"
title: "Фермагийн бага теорем"
date: "2018-05-04T14:56:26"
slug: "fermat-little"
permalink: "/2018/05/04/fermat-little/"
wordpress_id: 248
wordpress_url: "https://t8m8r.wordpress.com/2018/05/04/fermat-little/"
categories: ["Тооны онол", "теорем"]
tags: ["Ферма", "анхны тоо", "үелэх бутархай"]
status: "publish"
comments_count: 0
math: true
generated_by: "wordpress-importer"
templateEngineOverride: "md"
---

> **Фермагийн бага теорем.** \(a\) *нь эерэг бүхэл тоо* \(p\) *нь анхны тоо бол* \(a^p\equiv a\quad(\mathrm{mod}\, p).\)

*Баталгаа*. \(a=1\) үед теорем үнэн. Одоо \(a=n\) байх үед үнэн гэж үзээд, \(a=n+1\) тохиолдлыг сонирхоё.

\(\displaystyle (n+1)^p=\sum_{k=0}^p\binom{p}{k}n^k\)

Энд \(\displaystyle\binom{p}{k}=\frac{p!}{k!(p-k)!}\) нь мэдээж бүхэл. Мөн \(0\(\displaystyle (n+1)^p \equiv 1+n^p \equiv n+1\quad(\mathrm{mod}\, p)\)

болж теорем батлагдана.

**Жишээ.** \(p\) нь анхны тоо, \(0\(\beta^p\equiv \beta\quad(\mathrm{mod}\, p)\)

тул \(\beta^{p-1}-1\) нь \(p\)-д хуваагдана. Тэгэхээр \(\beta^{p-1}-1=kp\) гэвэл

\(\begin{array}{rcl}\displaystyle\frac{m}p&=&\displaystyle\frac{mk}{\beta^{p-1}-1}=\frac{mk}{\beta^{p-1}(1-\beta^{1-p})}=\frac{mk}{\beta^{p-1}}\big(1+\beta^{1-p}+\beta^{2(1-p)}+\ldots\big)\\&=&\displaystyle\frac{mk}{\beta^{p-1}}+\frac{mk}{\beta^{2(p-1)}}+\frac{km}{\beta^{3(p-1)}}+\ldots\end{array}\)

Одоо \(m\(10^6-1=7\cdot142857\)

(ө.х. \(k=142857\)) бөгөөд

\(\displaystyle\frac17=0.142857142857142857\ldots=0.\overline{142857}\)

байна.
