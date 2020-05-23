#
# Copyright 2018 Quantopian, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from datetime import time

import pandas as pd
from pandas.tseries.holiday import (
    Holiday,
    Easter,
    Day,
    GoodFriday,
    previous_friday,
)
from pytz import timezone

from calendars.common_holidays import corpus_christi


# Universal Confraternization (new years day)
ConfUniversal = Holiday(
    'Dia da Confraternizacao Universal',
    month=1,
    day=1,
)
# Sao Paulo city birthday
AniversarioSaoPaulo = Holiday(
    'Aniversario de Sao Paulo',
    month=1,
    day=25,
)
# Carnival Monday
CarnavalSegunda = Holiday(
    'Carnaval Segunda',
    month=1,
    day=1,
    offset=[Easter(), Day(-48)]
)
# Carnival Tuesday
CarnavalTerca = Holiday(
    'Carnaval Terca',
    month=1,
    day=1,
    offset=[Easter(), Day(-47)]
)
# Ash Wednesday (short day)
QuartaCinzas = Holiday(
    'Quarta Cinzas',
    month=1,
    day=1,
    offset=[Easter(), Day(-46)]
)
# Good Friday
SextaPaixao = GoodFriday
# Feast of the Most Holy Body of Christ
CorpusChristi = corpus_christi()
# Tiradentes Memorial
Tiradentes = Holiday(
    'Tiradentes',
    month=4,
    day=21,
)
# Labor Day
DiaTrabalho = Holiday(
    'Dia Trabalho',
    month=5,
    day=1,
)
# Constitutionalist Revolution
Constitucionalista = Holiday(
    'Constitucionalista',
    month=7,
    day=9,
    start_date='1998-01-01'
)
# Independence Day
Independencia = Holiday(
    'Independencia',
    month=9,
    day=7,
)
# Our Lady of Aparecida
Aparecida = Holiday(
    'Nossa Senhora de Aparecida',
    month=10,
    day=12,
)
# All Souls' Day
Finados = Holiday(
    'Dia dos Finados',
    month=11,
    day=2,
)
# Proclamation of the Republic
ProclamacaoRepublica = Holiday(
    'Proclamacao da Republica',
    month=11,
    day=15,
)
# Day of Black Awareness
ConscienciaNegra = Holiday(
    'Dia da Consciencia Negra',
    month=11,
    day=20,
    start_date='2004-01-01'
)
# Christmas Eve
VesperaNatal = Holiday(
    'Vespera Natal',
    month=12,
    day=24,
)
# Christmas
Natal = Holiday(
    'Natal',
    month=12,
    day=25,
)
# New Year's Eve
AnoNovo = Holiday(
    'Ano Novo',
    month=12,
    day=31,
    observance=previous_friday,
)

def holidays():
    return [
        ConfUniversal,
        AniversarioSaoPaulo,
        CarnavalSegunda,
        CarnavalTerca,
        SextaPaixao,
        CorpusChristi,
        Tiradentes,
        DiaTrabalho,
        Constitucionalista,
        Independencia,
        Aparecida,
        Finados,
        ProclamacaoRepublica,
        ConscienciaNegra,
        VesperaNatal,
        Natal,
        AnoNovo,
    ]

