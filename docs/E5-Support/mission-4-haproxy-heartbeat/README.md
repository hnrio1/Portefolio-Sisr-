# HAProxy & HeartBeat — Haute disponibilite

Mise en place d'une infrastructure **hautement disponible** avec **HeartBeat** (tolerance de panne) et **HAProxy** (repartition de charge) sur Debian 12.

<span class="tech-badge">HAProxy</span> <span class="tech-badge">HeartBeat</span> <span class="tech-badge">Debian 12</span> <span class="tech-badge">VRRP</span>

---

<div class="grid cards" markdown>

-   :material-target: __Objectifs__

    - Assurer la continuite de service en cas de panne
    - Repartir la charge sur plusieurs serveurs web
    - Configurer un IP virtuelle partagee
    - Tester le basculement automatique

-   :material-cog: __Configuration realisee__

    - 2 serveurs HAProxy en failover
    - Service HeartBeat pour detection panne
    - IP virtuelle (VIP) partagee
    - 2 serveurs web backend en load balancing

-   :material-school: __Competences mobilisees__

    - Haute disponibilite et tolerance de panne
    - Load balancing applicatif
    - Administration Linux avancee
    - Architecture redondante

</div>

---

## Compte rendu complet

<iframe src="./TP_HAProxy_HeartBeat_Henrio.pdf" width="100%" height="800px" style="border: none;"></iframe>

[:material-download: Telecharger le PDF](./TP_HAProxy_HeartBeat_Henrio.pdf){ target="_blank" .md-button .md-button--primary }
