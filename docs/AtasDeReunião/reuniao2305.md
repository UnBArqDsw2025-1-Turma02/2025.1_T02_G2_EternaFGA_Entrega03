# Reunião 23/05/2025 
**Início:** 21:10 | **Fim:** 23:00  

<!-- Substitua DD/MM/AAAA pela data e os horários reais da reunião -->

## Participantes Convocados

<!-- Tabela de presença com todos os participantes fixos do grupo -->

Na Tabela 1, são apresentados os participantes da reunião juntamente com os indicadores que demonstram se estão presentes ou não, onde ✅ significa que o participante está presente e ❌ significa que o participante não compareceu à reunião.

**Tabela 1: Participantes Convocados e Presença na Reunião**

| Nome                                      | Matrícula     | Presente        |
|-------------------------------------------|---------------|-----------------|
| Cairo Florenço Santos                     | 222014975     |✅ |
| Edilson Ribeiro da Cruz Júnior            | 222024461     |✅ |
| Maria Eduarda Vieira Monteiro             | 221008356     | ✅ |
| Gabriel Reis Scheidt Paulino             | 222015112     |✅  |
| Gustavo Feitosa Haubert                   | 222024793     | ✅ |
| Manuella Magalhães Valadares              | 222021890     | ✅  |
| Marcos Vieira Marinho                     | 222021906     | ✅ |
| Marcus Vinícius Figuerêdo Escobar         | 222006973     | ✅  |
| Mateus Henrique Queiroz Magalhães Sousa   | 222025950     | ❌ |
| Pedro Gois Marques Monteiro              | 222026386     | ✅  |
| William Bernardo da Silva                 | 222021933     | ❌ |

**Autor:** [Manuella Valadares](https://github.com/manuvaladares)

---

## Pautas

<!-- Liste os assuntos abordados na reunião -->
- Revisão e adaptação do diagrama de classes
- Discussão sobre criação de perfis de usuário e autenticação
- Definição entre galeria, coleção e exposição
- Análise do uso de padrões de projeto (Composite, Prototype, Strategy etc.)

---

## Decisões

<!-- Liste as decisões principais tomadas -->
1. Criação de uma estrutura de autenticação com a classe `Autenticador`, pensada como Singleton ou classe abstrata.
2. Introdução de perfis de usuário (estudante e administrador), com herança de uma classe abstrata `Usuário`.
3. Discussão da diferença entre visitante, galeria e coleção:
   - Visitante: sem login, apenas visualiza.
   - Galeria: pasta pessoal de memórias.
   - Coleção/Exposição: conjunto de memórias com significado, título, descrição.
4. O padrão de projeto `Composite` será explorado para modelar as exposições/coleções.
5. O padrão `Factory Method` poderá ser utilizado para instanciar os diferentes tipos de usuário (visitante, estudante, administrador).

---

## Compromissos

<!-- Tabela de responsabilidades futuras -->

| Compromisso                                                       | Data de Entrega        | Responsáveis                          | Revisores               |
|-------------------------------------------------------------------|-------------------------|----------------------------------------|-------------------------|
| Adaptação do diagrama de classes com base nas decisões da reunião | Próxima reunião geral  | Todos os integrantes presentes         | Subgrupo responsável    |
| Implementação da estrutura de autenticação (`Autenticador`)       | A combinar              | Edilson                                | Manuella e Marcos       |
| Definição formal dos métodos de `Visitante`, `Usuário`, `Estudante` e `Administrador` | Em andamento contínuo | Marcus, Gustavo e Manuella             | Subgrupo                |
| Documentação da lógica de exposições e coleções                   | Durante a semana        | Cairo, Escobar                         | Manuella e Maria Eduarda|

---

## Gravação da reunião

<iframe width="560" height="315" src="https://www.youtube.com/embed/6n92doooXRQ?si=Iv0Cp9pT1YT0m6pw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

## Histórico de versões

| Versão | Data     | Descrição                        | Autor(es) | Revisor(es) | Comentário do Revisor |
|--------|----------|----------------------------------|-----------|-------------|------------------------|
| `1.0`  | 23/05/25 | Criação da ata da reunião        | Manuella  | —           | —                      |