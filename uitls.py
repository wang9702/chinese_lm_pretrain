# -*- coding:utf-8 -*-
import re


def translate_text(text, char_to_roman: bool = True):
    table = {
        ord(f): ord(t) for f, t in zip(u'""‘’′;:,!?[]()＜＞～％＃＠＆—－１２３４５６７８９０', u'“”\'\'\'；：，！？【】（）<>~%#@&--1234567890')
    }
    text = text.translate(table)
    number_mapping = {
        "viii": "ⅷ",
        "iii": "ⅲ",
        "vii": "ⅶ",
        "ii": "ⅱ",
        "iv": "ⅳ",
        "vi": "ⅵ",
        "ix": "ⅸ",
        "i": "ⅰ",
        "v": "ⅴ",
        'x': "ⅹ",
    }

    for k, v in number_mapping.items():
        text = re.sub(v.upper(), k.upper(), text)

    if char_to_roman:
        mask_char = list({"@", "￥", "&", "%", "#"}.difference(set(list(text))))[0]
        for k, v in number_mapping.items():
            search_k = re.finditer(k, text)
            mask_text = mask_char * len(k)
            for _search in search_k:
                s = _search.start()
                e = _search.end()
                if ((0 <= s - 1 < len(text) and not "\u4e00" <= text[s - 1] <= "\u9fa5") or s - 1 == -1) or (
                    (e < len(text) and not "\u4e00" <= text[e] <= "\u9fa5") or e == len(text)
                ):
                    text = text[:s] + mask_text + text[e:]
            text = re.sub(k, v, text)
            text = re.sub(mask_text, k, text)
    return text


def clean_space(text):
    text = re.sub('-+', '-', text)
    text = re.sub(r'[\n\r\t]', '', text)
    match_regex = re.compile(r'[\u4e00-\u9fa5\.,:《》、\(\)] +|[a-z A-Z\d]+')
    should_replace_list = match_regex.finditer(text)

    cleaned_text = ""
    start, end = 0, 0
    for chunk in should_replace_list:
        end = chunk.span()[0]
        cleaned_text += text[start:end]
        start = chunk.span()[1]

        chunk_text = chunk.group()
        chunk_text = chunk_text.strip()
        chunk_text = re.sub(" +", " ", chunk_text)
        cleaned_text += chunk_text
    cleaned_text += text[start:]
    cleaned_text = ' '.join(cleaned_text.split())
    return cleaned_text


def convert_symbol(text):
    sub_list = re.findall(r'\D(\.)\D', text)
    if sub_list:
        for sub in sub_list:
            text = text.replace(sub, '、')
    return text


def clean_html(text):
    pattern = [r'(<.*?>).*?(</.*?>)', r'<.*?/>', r'</.*?>', r'<img.*?>']
    for p in pattern:
        sub_list = re.findall(p, text)
        if sub_list:
            for sub in sub_list:
                if isinstance(sub, str):
                    text = text.replace(sub, '')
                else:
                    for s in sub:
                        text = text.replace(s, '')
    return text


def clean_greek(text):
    greek_lower = [chr(ch) for ch in range(945, 970) if ch != 962]
    greek_upper = [chr(ch) for ch in range(913, 937) if ch != 930]
    greek_englist = ["alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta", "theta", "iota", "kappa", "lambda",
                     "mu", "nu", "xi", "omicron", "pi", "rho", "sigma", "tau", "upsilon", "phi", "chi", "psi", "omega"]
    greek_map = {ch: greek_englist[idx % 24] for idx, ch in enumerate(greek_lower + greek_upper)}
    new_text = ""
    for ch in text:
        if ch in greek_map:
            new_text = new_text + greek_map[ch]
        else:
            new_text = new_text + ch
    return new_text


def format_text(text):
    text = translate_text(text)
    text = clean_space(text)
    text = clean_greek(text)
    text = clean_html(text)
    text = convert_symbol(text)
    return text


if __name__ == '__main__':

    s = '再经过喉腔.咽腔.鼻腔及胸腔的共鸣作用'
    # res = re.findall(r'[\u4e00-\u9fa5](\.)[\u4e00-\u9fa5]', s)
    s = format_text(s)
    # print(res)
    print(s)