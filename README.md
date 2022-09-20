# Backupscript
Dette backupscript benytter sig af Microsoft XCopy funktionalitet, til at hjælpe dig med at sikre dine filer, ved at back disse op til en backuplokation.

## "Brugsanvisning"
Brugen af scriptet er ganske simpelt, du følger ganske simpelt instruktionerne på skærmen, men der er en række begreber du som bruger bør forstå, før du går igang.

## Backup termenologi
En backup er ikke det samme som simpelt at gemme en fil, det er at kopiere en fil til en sekundær lokation, således dine filer er sikret, i tilfælde af system nedbrud.
Dette script har en prædefineret lokation for backup, så hvis de filer du vælger at tage backup af ligger på samme drev, så er du IKKE sikret i tilfælde af at dette drev går ned.
## Backup Typer
Scriptet kan foretage 2 former for backup, en **Full backup**, eller en **Differential backup**
### Full Backup
En Full backup betyder at samtlige filer i det directory du vælger, vil blive lagt over i backup mappen. Filer der allerede ligger på destinationen vil blive overskrevet, såfremt en nyere version findes på source. Det foreslås på det kraftigste, at foretage en full backup med jævne mellemrum.
### Differential backup
Med denne backup type vil der kun blive taget backup af nye filer, eller filer, der ikke allerede ligger på destinationen. På denne måde behøver du ikke vente på at kopiere filer, som allerede er backed up. **Bemærk** at filer med identiske navne på source og destination **vil** blive backed up, såfremt dem på source lokationen har været ændret for kortere tid siden, end dem på destinationen.

## Advarsler

**Bemærk** at hvis en fil på destinationen har samme navn som en fil i source, **og** den på destinationen er nyere, vil din fil **ikke** overskrive den på destinationen. Af denne grund anbefales det at dette script **ikke** benyttes til kollaberativt arbejde.
Hvis brugeren på trods af dette ønsker at benytte scriptet til kollaberativt arbejde, anbefales det at medlemmerne af arbejdsgruppen designer et navngivnings-schema, således uønskede tab af filer undgås. **Forfatter af dette script påtager sig intet ansvar for filtab i forbindelse med kollaberativt arbejde**

Dette script er **ikke** fuld-automatisk, og du skal køre scriptet manuelt **Hver gang** du ønsker at foretage backup.

Dette script kræver **brugerinput** for at udføre sin funktion, og er derfor **ikke velegnet til at blive automatiseret** via for eksempel Windows Task Scheduler.

Når konsollen viser outputtet **processing........**, hver her opmærksom på, at operationen er **kodet til at tage 8 sekunder**, og du kan **ikke** reducere denne tid ved at opgradere hardwaren i din maskine. Forfatter af scriptet står inde for, at brugen af scriptet er ***cirka*** 80 procent mere "hacker-film-fra-halvfemserne" agtigt med denne forsinkelse, og denne er derfor ikke et feature, som scripted kan anses for værende funktionel foruden. 
