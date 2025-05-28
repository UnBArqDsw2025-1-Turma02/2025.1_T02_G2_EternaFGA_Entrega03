# Reunião 28/05/2025  
**Início:** 20:20 | **Fim:** 20:45 

## Participantes Convocados

<!-- ✅ = presente | ❌ = ausente -->

**Tabela 1: Participantes Convocados e Presença na Reunião**

| Nome                                      | Matrícula     | Presente |
|-------------------------------------------|---------------|----------|
| Manuella Magalhães Valadares              | 222021890     | ✅       |
| Marcos Vieira Marinho                     | 222021906     | ✅       |
| Mateus Henrique Queiroz Magalhães Sousa   | 222025950     | ✅       |
| William Bernardo da Silva                 | 222021933     | ✅       |

**Autor:** [Manuella Valadares](https://github.com/manuvaladares)

---

## Pautas

- Apresentação das versões individuais do padrão **Composite**
- Discussão sobre uso de `Memória` como Composite ou criação de nova classe
- Alinhamento e consolidação do diagrama final
- Ajustes de atributos (ex: legenda, URL, duração)
- Planejamento das tarefas restantes: interface, documentação, entrega

---

## Decisões

1. O grupo decidiu utilizar a classe `Memória` como Composite no padrão estrutural.
2. Houve revisão e alinhamento entre os diagramas e códigos de Mateus e Manuella, que estavam bastante semelhantes.
3. As pequenas diferenças nos atributos e localização de propriedades foram padronizadas:
   - `legenda` no lugar de `descrição`
   - `URL do arquivo` permanece nas folhas (`Vídeo`, `Imagem`)
4. Foi validada a cardinalidade: uma `Memória` pode conter uma ou mais mídias, e cada `MídiaDigital` pertence a uma `Memória`.
5. A versão final do diagrama será baseada no de Manuella.
6. Marcos ficará responsável por montar a **interface gráfica**.
7. Mateus será responsável pela **documentação** da entrega.
8. Manuella ficou encarregada de subir a ata.
9. William gravará sua parte da entrega pois não poderá estar presente na próxima reunião.
10. Será realizada uma reunião geral com todos os subgrupos no sábado para integrar as partes da entrega final.

---

## Compromissos

| Compromisso                                                        | Data de Entrega       | Responsáveis                  | Revisores             |
|--------------------------------------------------------------------|------------------------|-------------------------------|------------------------|
| Finalizar e revisar diagrama do padrão Composite                  | Antes da próxima reunião | Manuella                      | Subgrupo               |
| Montagem da interface gráfica (HTML)                              | Até sexta-feira         | Marcos Vieira Marinho         | —                      |
| Gravação da entrega (parte do William)                            | Até sexta-feira         | William Bernardo da Silva     | —                      |
| Documentação técnica da entrega                                   | Durante a semana        | Mateus Henrique               | —                      |
| Subida da ata                                                     | Imediato                | Manuella Valadares            | —                      |
| Reunião geral com todos os subgrupos                              | Sábado (01/06)          | Todos os integrantes          | —                      |

---

## Gravação da reunião

<iframe width="560" height="315" src="https://www.youtube.com/embed/oys5FtmcPP8?si=GxhOKoFWRsfiC6UL" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

## Histórico de versões

| Versão | Data     | Descrição                     | Autor(es) | Revisor(es) | Comentário do Revisor |
|--------|----------|-------------------------------|-----------|-------------|------------------------|
| `1.0`  | 28/05/25 | Criação da ata da reunião     | Manuella  | —           | —                      |
