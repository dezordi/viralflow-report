# viralflow-report

This directory contains the code to sumarize html results of ViralFlow 1.0.0

## install

```bash
git clone https://github.com/dezordi/viralflow-report.git
pip install .
```

## run

```bash
#help message
vfreports --help

#passing a dir with all htmls:
vfreports <path_to_htmls> <output_dir>

#passing a base dir with glob regex to capture html files on sub-drectories
vfreports --glob-fastp "*/*fastp.html" --glob-snpeff "*/*snpEff*.html" <path_to_base_dir> <output_dir>
```

## output directory structure
After run, the vfreports will generate a directory with the output content, the results will present on index.html
```
#example
.
├── css
│   └── style.css
├── htmls
│   ├── ART1_R1.fastp.html
│   ├── ART2_R1.fastp.html
│   └── Cneg_R1.fastp.html
└── index.html  #file with results
```
