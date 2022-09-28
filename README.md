# Brugerdrevet Backupscript
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

# Automatisk Backupscript
Dette backupscript benytter sig af den samme XCOPY funktion, som i den brugerdrevne version. Forskellen på de to er, at dette script ikke krever input fra brugeren på noget tidspunkt, men i stedet aflæser dags dato fra dit system, hvorefter der foretages full backup Tirsdag og Torsdag, mens der alle andre dage foretages en differential backup. Se ovenstående afsnit om **Backup termenologi**, for indblik i forskellen på de to backup typer.

## Brugsanvisning
Dette script er tiltænk brug i sammenhæng med windows task scheduler. Når scriptet køres vil der blive foretaget en backup, såfremt python er installeret på systemet.
For info omkring opsætning af Task Scheduler, henvises der til denne guide af Jean-Christophe Chouinard, på hans hjemmeside her: **https://www.jcchouinard.com/python-automation-using-task-scheduler/**

Det anbefales at scripted skemalægges til at køre på at fastsat tidspunkt, for eksempel:
1: Før fastlagte pauser
2: Før fyraften
3: Før planlagt systemvedligeholdelse

## Advarsler
Hver opmærksom på, at dette script benytter datetime fra **det system det køres på**. Hvis tid ikke er synkroniseret på tværs af maskiner som dette script køres på, kan der forekommer afvigelser af hvilke dage diverse maskiner foretager henholdsvist full og differential backup.

Windows Task Scheduler besider ikke en mulighed for at foretage en task i forbindelse med nedlukning af systemet. Dette betyder bruger skal være opmærksom på, at der kan være gået markant tid siden sidste foretagede backup, når systemet lukkes ned. 

Opgradering fra Windows 10 til Windows 11 har for visse brugere ført til tab at scheduled tasks, hver opmærksom på dette ved opgradering, og tjek at scriptet stadig er skemalagt, efter opgraderingen er fuldendt.

Skift af licensnøgle har for visse brugere medført tab af scheduled tasks, så det anbefales at der tjekkes for om scripted stadig er skemalagt, i forbindelse med alle skift af licens nøgler.
