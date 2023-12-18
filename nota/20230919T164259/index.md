# Gerando pdfs com xelatex

No arquivo `.Rnw` foram inseridos _non-printable unicode characters_ obtidos [aqui](https://www.soscisurvey.de/tools/view-chars.php).

Para executar um container baseado na [imagem docker da ploa 2024](https://hub.docker.com/r/fjuniorr/volumes) abra o programa Docker Desktop e depois execute no terminal:


```bash
docker run --rm -p 8787:8787 -ti --mount type=bind,source=$(PWD),target=/home/rstudio volumes:ploa2024 bash
```

Dentro do container execute:

```bash
R CMD Sweave --pdf table.Rnw 
```

```bash
pdfinfo table.pdf 
Creator:        TeX
Producer:       pdfTeX-1.40.19
CreationDate:   Tue Sep 19 19:56:43 2023 UTC
ModDate:        Tue Sep 19 19:56:43 2023 UTC
Tagged:         no
UserProperties: no
Suspects:       no
Form:           none
JavaScript:     no
Pages:          1
Encrypted:      no
Page size:      612 x 792 pts (letter)
Page rot:       0
File size:      29704 bytes
Optimized:      no
PDF version:    1.5
```

Inicia sessão do Rstudio em http://localhost:8787/ (usuário: rstudio, senha: splor)

```
docker exec -d -e PASSWORD=splor volumes-loa /init
```

## Links

- [Avaliar substituição de pdflatex por xelatex ou lualatex · Issue #53 · splor-mg/volumes-loa](https://github.com/splor-mg/volumes-loa/issues/53)
- [Customizing LaTeX Options in the RStudio IDE – Posit Support](https://support.posit.co/hc/en-us/articles/200532257)
- [Using Sweave and knitr – Posit Support](https://support.posit.co/hc/en-us/articles/200552056)
- [r - Difference: "Compile PDF" button in RStudio vs. knit() and knit2pdf() - Stack Overflow](https://stackoverflow.com/questions/34591487/difference-compile-pdf-button-in-rstudio-vs-knit-and-knit2pdf)
- [latex - Running xelatex programmatically from R script - Stack Overflow](https://stackoverflow.com/questions/49082874/running-xelatex-programmatically-from-r-script)
- [tips/tex/tex-tips.Rmd at master · jrminter/tips](https://github.com/jrminter/tips/blob/master/tex/tex-tips.Rmd#L859)
- [xetex - How to use texi2dvi to run latex generating PDF? - TeX - LaTeX Stack Exchange](https://tex.stackexchange.com/questions/31808/how-to-use-texi2dvi-to-run-latex-generating-pdf)
- [Forbidden control sequence found when knitting the minimal example · Issue #375 · rstudio/bookdown](https://github.com/rstudio/bookdown/issues/375)
- [R Manuals :: R Internals - 11  Use of TeX dialects](https://rstudio.github.io/r-manuals/r-ints/Use-of-TeX-dialects.html)

    `tools::texi2dvi` makes use of a system command `texi2dvi` where available. On a Unix-alike this is usually part of `texinfo`, whereas on Windows if it exists at all it would be an executable, part of MiKTeX. If none is available, the R code runs a sequence of `(pdf)latex`, `bibtex` and `makeindex` commands.

- Sweave now outputs ‘.tex’ files in UTF-8 if the input encoding is declared to be UTF-8, regardless of the local encoding. The UTF-8 encoding may now be declared using a LaTeX comment containing the string %\SweaveUTF8 on a line by itself.

