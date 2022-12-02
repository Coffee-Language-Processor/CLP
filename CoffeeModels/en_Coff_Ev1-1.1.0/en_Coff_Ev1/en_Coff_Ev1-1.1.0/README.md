A natural language processor API for coffee drinks in all forms

| Feature | Description |
| --- | --- |
| **Name** | `en_Coff_Ev1` |
| **Version** | `1.1.0` |
| **spaCy** | `>=3.4.3,<3.5.0` |
| **Default Pipeline** | `tok2vec`, `ner` |
| **Components** | `tok2vec`, `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | n/a |
| **Author** | [Chris Bruinsma,Iris Chi,Jack Felciano,Jeffrey Li,Dustin Paden]() |

### Label Scheme

<details>

<summary>View label scheme (13 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `Anti`, `drink`, `extra`, `milk`, `milk texture`, `pump quantity`, `roast`, `shot quality`, `shot quantity`, `size`, `syrup`, `temperature`, `toppings` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 99.11 |
| `ENTS_P` | 99.07 |
| `ENTS_R` | 99.15 |
| `TOK2VEC_LOSS` | 15306.96 |
| `NER_LOSS` | 146275.12 |