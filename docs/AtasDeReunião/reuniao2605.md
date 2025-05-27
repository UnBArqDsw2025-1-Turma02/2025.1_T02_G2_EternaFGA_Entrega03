# Reunião 26/05/2025  
**Início:** 21:10 | **Fim:** 22:20 

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

- Correções no diagrama de classes com base em versões anteriores e prints.
- Ajustes de atributos: adição de `textoAlternativo`, `duração`, entre outros.
- Discussão sobre uso de interfaces e classes abstratas.
- Validação do uso do padrão de projeto Factory Method.
- Apresentação dos códigos individuais dos integrantes.
- Início da construção de um diagrama consolidado e interface gráfica.
- Planejamento das próximas etapas.

---

## Decisões

1. Adição de atributos que estavam ausentes no diagrama anterior, como `textoAlternativo` e `duração`, com definição de tipos apropriados.
2. **Decisão sobre duração**: utilizar `string` em vez de `int`, considerando limitações práticas.
3. A classe `Usuário` deixará de ser uma interface e passará a ser uma classe abstrata, para permitir atributos.
4. **Padrão Factory Method**: Confirmada sua aplicação com métodos como `criarMídia()` retornando `MídiaDigital`.
5. O `gerenciador de fábrica` será removido por não estar sendo utilizado.
6. Os códigos individuais dos membros estão funcionando e serão integrados em uma versão conjunta.
7. O grupo acordou que a versão final do código será baseada na estrutura combinada das implementações já realizadas.
8. Planejamento da divisão de tarefas finais, incluindo documentação e criação da interface HTML.

---

## Compromissos

| Compromisso                                           | Data de Entrega        | Responsáveis                          | Revisores               |
|-------------------------------------------------------|-------------------------|----------------------------------------|-------------------------|
| Consolidar e revisar o diagrama de classes final      | Durante a semana        | Manuella, Marcos, Mateus, William      | Subgrupo completo       |
| Atualizar atributos no código conforme o diagrama     | Durante a semana        | Todos os integrantes presentes         | Subgrupo completo       |
| Construção da interface HTML e campos do formulário   | Até próxima reunião     | Marcos Vieira Marinho                  | —                       |
| Documentação da reunião e decisões tomadas            | Até próxima reunião     | Manuella Valadares                     | —                       |
| Atualizar texto explicativo no PDF (metodologia)      | Durante a semana        | Mateus Henrique                        | —                       |
| Reunião futura para abordar o padrão estrutural       | 27/05/2025              | Todos os integrantes                   | —                       |

---

## Gravação da reunião

<iframe width="560" height="315" src="https://www.youtube.com/embed/SrvTdzcHErc?si=f8BskTy7jI72zOhI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

## Histórico de versões

| Versão | Data     | Descrição                        | Autor(es) | Revisor(es) | Comentário do Revisor |
|--------|----------|----------------------------------|-----------|-------------|------------------------|
| `1.0`  | 26/05/25 | Criação da ata da reunião        | Manuella  | —           | —                      |
