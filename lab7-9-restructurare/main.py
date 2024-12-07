from infrastructura.repository_evenimente import RepositoryEvenimente, RepositoryEvenimenteFaraFisier
from infrastructura.repository_participanti import RepositoryParticipanti, RepositoryParticipantiFaraFisier
from infrastructura.repository_persoane import RepositoryPersoane, RepositoryPersoaneFaraFisier
from prezentare.consola import Ui
from business.service_persoane import ServicePersoane
from business.service_evenimente import ServiceEvenimente
from business.service_participanti import ServiceParticipanti
from validare.validator_evenimente import ValidatorEvenimente
from validare.validator_persoane import ValidatorPersoane
from testare.teste import Teste
from application_coordinator import repositoryCuFisiere


teste = Teste()

if repositoryCuFisiere:
    repository_persoane = RepositoryPersoane('infrastructura/fisier_persoane.txt')
    repository_evenimente = RepositoryEvenimente('infrastructura/fisier_evenimente.txt')
    repository_participanti = RepositoryParticipanti('infrastructura/fisier_participanti.txt')
else:
    repository_persoane = RepositoryPersoaneFaraFisier()
    repository_evenimente = RepositoryEvenimenteFaraFisier()
    repository_participanti = RepositoryParticipantiFaraFisier()

validator_persoane = ValidatorPersoane()
validator_evenimente = ValidatorEvenimente()

service_persoane = ServicePersoane(validator_persoane, repository_persoane, repository_participanti)
service_evenimente = ServiceEvenimente(validator_evenimente, repository_evenimente, repository_participanti)
service_participanti = ServiceParticipanti(validator_persoane, validator_evenimente, repository_persoane, repository_evenimente, repository_participanti, service_persoane, service_evenimente)


def main():
    teste.ruleaza_toate_testele()
    run = Ui(service_persoane, service_evenimente, service_participanti)
    run.run()

if __name__ == '__main__':
    main()