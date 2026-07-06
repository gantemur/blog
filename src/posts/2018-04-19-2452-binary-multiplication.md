---
layout: "layouts/post.njk"
title: "Үржүүлэх алгоритм"
date: "2018-04-19T01:31:44"
slug: "binary-multiplication"
permalink: "/2018/04/19/binary-multiplication/"
wordpress_id: 2452
wordpress_url: "https://t8m8r.wordpress.com/2018/04/19/binary-multiplication/"
categories: ["алгоритм", "компьютер"]
tags: ["бит", "хоёртын тоолол", "үржүүлэх"]
status: "publish"
comments_count: 0
math: true
generated_by: "wordpress-importer"
templateEngineOverride: "md"
---

Хоёртын тоололд \\(a\\), \\(b\\) гэсэн хоёр тоог үржүүлэх алгоритмыг дорх зурагт дүрслэв. Энд \\(n\\) бүхэл тоо нь \\(a = 2^n + \ldots\\) гэсэн шинжээр тодорхойлогдоно. Тэгээд \\(a\\) тооныхоо битүүдийг харж байгаад \\(b\\)-гээ нэмээд нэмээд явчихна. Энд зөвхөн нэмэх, бит шилжүүлэх үйлдлүүд л орно.

[![](/blog/assets/wp-media/2018/04/multbin.png)](/blog/assets/wp-media/2018/04/multbin.png)

Тодруулбал, эхлээд \\(\pi_0=0\\) гэж аваад, дараах рекуррент томъёог ашиглан \\(ab\\) үржвэрийг \\(ab=\pi_{n+1}\\) гэж олох юм.

\\(\pi_{j+1} =
\begin{cases}
\pi_{j} &\textrm{if}\,\,a_j=0 ,\\
\pi_{j}+2^j b &\textrm{if}\,\,a_j=1 .
\end{cases}\\)
