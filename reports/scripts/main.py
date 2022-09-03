import click
import re
import os
import glob
from pathlib import Path as path
from reports.base_html import (
    CSS,
    HEADER,
    FOOTER
)

def get_snpeff_code(html_file):
    sample_code = str(re.findall(".*\.vcf", open(html_file).read()))
    sample_code = re.sub(r".*\s", "", sample_code)
    sample_code = re.sub(r"\.vcf.*", "", sample_code)
    return sample_code

def get_fastp_code(html_file):
    sample_code = str(re.findall(".*-i.*", open(html_file).read()))
    sample_code = re.sub(r".*\s-i\s", "", sample_code)
    sample_code = re.sub(r"_.*", "", sample_code)
    return sample_code

def get_body(sample_codes, title):
    sample_line = ""
    sample_line += str(title)
    sample_line += "\t\t\t\t<div class='row'>\n"
    for sample, path in sample_codes.items():
        sample_line += f"\t\t\t\t\t<div class='column'><a href = '{path}'> {sample} </a></div>\n"
    sample_line += "\t\t\t\t</div>\n"
    return sample_line

def write_index_html(fastp_codes, snpeff_codes):
    body_fastp = get_body(fastp_codes, "\t\t\t<h2>fastp</h2>\n")
    body_snpeff = get_body(snpeff_codes, "\t\t\t<h2>snpEff</h2>\n")
    return HEADER+body_fastp+body_snpeff+FOOTER

@click.group()
def cli():
    pass

@cli.command()
@click.option('--glob-fastp', 
               type=str,
               default="/*fastp.html",
               help="Regex to found fastp html files from path base.")
@click.option('--glob-snpeff', 
               type=str,
               default="/*snpEff*.html",
               help="Regex to found snpeff html files from path base.")
@click.argument('path-base')
@click.argument('path-out')
def main(glob_fastp, glob_snpeff, path_base, path_out):
    path_out = re.sub(r"\/$", "", path_out)
    os.mkdir(path_out)
    os.mkdir(f"{path_out}/htmls")
    os.mkdir(f"{path_out}/css")
    os.system(f"cp {CSS} {path_out}/css/")
    files_snpeff = path(path_base).glob(glob_snpeff)
    files_fastp = path(path_base).glob(glob_fastp)
    fastp_codes = {}
    snpeff_codes = {}
    for html_file in files_fastp:
        os.system(f"cp {html_file} {path_out}/htmls/")
        html_file = re.sub(r".*\/", "", str(html_file))
        fastp_codes[get_fastp_code(f"{path_out}/htmls/{html_file}")] = f"./htmls/{html_file}"
    for html_file in files_snpeff:
        os.system(f"cp {html_file} {path_out}/htmls/")
        html_file = re.sub(r".*\/", "", str(html_file))
        snpeff_codes[get_snpeff_code(f"{path_out}/htmls/{html_file}")] = f"./htmls/{html_file}"
    
    with open(f"{path_out}/index.html", "w") as file:
        file.write(write_index_html(fastp_codes, snpeff_codes))