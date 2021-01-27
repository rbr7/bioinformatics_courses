#!/usr/bin/env python3

import sys
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", help="fold number to specify nucleotide/amino acid sequence length per line")
parser.add_argument("-i", help="input file name")
args = parser.parse_args()

base_aa_ext = '.faa'
base_na_ext = '.fna'
file_iden = {'embl': 'ID','fastq': '@','genbank': 'LOCUS','mega': '#MEGA','vcf': '##fileformat','sam': '@'}

def find_format(file_name: str):
    # do something
    with open(file_name, 'r') as fh:
        file = fh.readlines()
    file_mark, marker = list(), list()
    for line in file:
        for k, v in file_iden.items():
            if line.startswith(v):
                file_mark.append(k)
                marker.append(v)
        break

    if len(file_mark) > 1 and '@' in marker:
        for line in file:
            if line.startswith('@') and file[2].startswith('+'):
                file_mark = ['fastq']
                break
            elif line.startswith('@SQ') or line.startswith('@PG'):
                file_mark = ['sam']
                break
            else:
                continue
                
    return file_mark[0]

class convert_file_to_fasta:
    def __init__(self):
        pass

    def embl(self, data: list, fold: int, filename: str):
        #
        embl_sym = ['ID', 'AC', 'DE', 'SQ', '//']
        file_extract = {'id': None, 'acc': None, 'descr': None, 'len': None}
        idx = {'start': None, 'end': None}
        for line in data:
            for sym in embl_sym:
                if line.startswith(sym):
                    if sym == 'ID':
                        file_extract['id'] = line.split()[1].replace(';', '')
                    elif sym == 'AC':
                        file_extract['acc'] = line.split()[1].replace(';', '')
                    elif sym == 'DE':
                        file_extract['descr'] = line.rstrip()[2:].strip()
                    elif sym == 'SQ':
                        file_extract['len'] = re.search('Sequence(.+?)BP', line).group(1).strip()
                        idx['start'] = data.index(line)
                    elif sym == '//':
                        idx['end'] = data.index(line)
        hdr = '>' + file_extract['id'] + ' |acc=' + file_extract['acc'] + '|descr=' + file_extract['descr'] + '|len=' + file_extract['len']
        d = data[idx['start']+1:idx['end']]
        seq = ''
        for line in d:
            ll = line.split()
            for t in ll:
                if set(t) <= set('ACGTNacgtn'):
                    seq = seq + t.replace(" ", "")
                    file_ext = base_na_ext
                elif t.rstrip().isdigit():
                    continue
                else:
                    seq = seq + t.replace(" ", "")
                    file_ext = base_aa_ext
        res = [seq.upper()[i:i + fold] for i in range(0, len(seq.upper()), fold)]
        result = [hdr] + res
        ans = []
        for line in result:
            ans.append(line + '\n')
        result_file = str('.'.join(filename.split('.')[:-1]))+file_ext
        with open(result_file,'w') as fh:
            fh.writelines(ans)
        return

    def fastq(self, data: list, fold: int, filename: str):
        #
        res = []
        for l in data:
            if l.startswith('@'):
                res.append('>' + l[1:])
                mark = 1
            elif mark:
                result = [l.rstrip().upper()[i:i + fold]+'\n' for i in range(0, len(l.upper()), fold)]
                if set(result[0].rstrip()) <= set('ACGTNacgtn'):
                    file_ext = base_na_ext
                else:
                    file_ext = base_aa_ext
                res = res+result
                mark = 0
        result_file = str('.'.join(filename.split('.')[:-1])) + file_ext
        with open(result_file, 'w') as fh:
            fh.writelines(res)
        return

    def genbank(self, data: list, fold: int, filename: str):
        #print('yippie : ', data)
        res = []
        pos = {'start': None, 'end': None}
        for l in data:
            if l.startswith('DEFINITION') or l.startswith('VERSION'):
                res.append(l)
            elif l.startswith('ORIGIN'):
                pos['start'] = data.index(l)
            elif l.startswith('//'):
                pos['end'] = data.index(l)
        seq = ''
        for l in data[pos['start']+1:pos['end']]:
            ll = l.split()
            for t in ll:
                if set(t) <= set('ACGTNacgtn'):
                    seq = seq + t.replace(" ", "")
                    file_ext = base_na_ext
                elif t.rstrip().isdigit():
                    continue
                else:
                    seq = seq + t.replace(" ", "")
                    file_ext = base_aa_ext
        res = [seq.upper()[i:i + fold] for i in range(0, len(seq.upper()), fold)]
        lines = '>' + re.sub('VERSION', '', res[1]).strip() + ' ' + re.sub('DEFINITION', '', res[0]).strip()
        result = [lines + '\n'] + [l + '\n' for l in res]
        result_file = str('.'.join(filename.split('.')[:-1])) + file_ext
        with open(result_file, 'w') as fh:
            fh.writelines(result)
        return

    def mega(self, data: list, fold: int, filename: str):
        #
        mark = 0
        res4 = []
        hdr = []
        for l in data:
            if l.startswith('TITLE'):
                mark = 1
            elif l.startswith('#') and mark:
                if len(l.split()) == 1:
                    hdr.append('>' + l[1:])
                else:
                    continue
            elif len(l.rstrip()) != 0:
                if set(l.rstrip()) <= set('ACGTNacgtn'):
                    res4.append(l)
                    file_ext = base_na_ext
                else:
                    res4.append(l)
                    file_ext = base_aa_ext
        res4 = ''.join(res4)
        res = [res4.rstrip().upper()[i:i + fold]+'\n' for i in range(0, len(res4), fold)]
        result = hdr+res
        result_file = str('.'.join(filename.split('.')[:-1])) + file_ext
        with open(result_file, 'w') as fh:
            fh.writelines(result)
        return

    def vcf(self, data: list, fold: int, filename: str):
        #
        res6 = []
        mark = 0
        for l in data:
            if l.startswith('#CHROM'):
                res6.append(l)
                mark = 1
            elif not l.startswith('#') and mark:
                res6.append(l)
        ref = []
        for r in res6[1:]:
            ref.append(r.split('\t')[3])
        ref = ''.join(ref)
        res = [ref.rstrip().upper()[i:i + fold]+'\n' for i in range(0, len(ref.upper()), fold)]
        res = ['>'+res6[1].split('\t')[0]+'\n']+res
        if set(res[1].rstrip()) <= set('ACGTNacgtn'):
            file_ext = base_na_ext
        else:
            file_ext = base_aa_ext

        arr = []
        for r in res6[1:]:
            arr.append([r.split('\t')[3]] + r.split('\t')[4].split(','))
        vcf_res = []
        i = 0
        for sample in [x for x in res6[0].split()[9:] if x.startswith('sample')]:
            hdr = ['>' + sample]
            j = 0
            arr2 = []
            for l in res6[1:]:
                pos = l.split('\t')[9 + i][0]
                seq = arr[j][int(pos)]
                arr2.append(seq)
                j += 1
            hdr.append(''.join(arr2))
            vcf_res.append(hdr)
            i += 1
        res2 = []
        for l in vcf_res:
            k = l[0]+'\n'
            k2 = [l[1].rstrip().upper()[i:i + fold] + '\n' for i in range(0, len(l[1].upper()), fold)]
            k3 = [k]+k2
            res2 = res2+k3
        result = res + res2
        result_file = str('.'.join(filename.split('.')[:-1])) + file_ext
        with open(result_file, 'w') as fh:
            fh.writelines(result)
        return

    def sam(self, data: list, fold: int, filename: str):
        #
        res5 = []
        for l in data:
            if not l.startswith('@') and len(l.split()) >= 11:
                res5.append('>' + l.split()[0]+'\n')
                n = fold
                seq = l.split()[9]
                res = [seq.rstrip().upper()[i:i + n]+'\n' for i in range(0, len(seq.upper()), n)]
                res5 = res5 + res
        if set(res5[1].rstrip()) <= set('ACGTNacgtn'):
            file_ext = base_na_ext
        else:
            file_ext = base_aa_ext
        result_file = str('.'.join(filename.split('.')[:-1])) + file_ext
        with open(result_file, 'w') as fh:
            fh.writelines(res5)
        return


if __name__ == '__main__':
    fold = 70
    file_type = find_format(args.i)
    with open(args.i, 'r') as fh:
        file = fh.readlines()
    converter_obj = globals()['convert_file_to_fasta']()
    func = getattr(converter_obj, file_type)
    if args.f:
        fold = args.f
    func(file, int(fold), args.i)
    # do something