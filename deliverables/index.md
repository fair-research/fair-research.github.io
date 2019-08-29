---
layout: default
title: FAIR Research Data - NIH Deliverables
---

# NIH Deliverables

Work supporting the [NIH Data Commons Pilot Phase Consortium](https://www.nihdatacommons.us).

*  [Ingesting metadata from NIH Common Fund Data Coordinating Centers](cfde-metadata-ingest.html) :
   Overview and current status of our work ingesting data manifests from NIH Common Fund research initiatives.
*  [Scalable, Cost-Controlled Analysis for Data Enrichment](scalable-analysis.html) :
   Example highlighting Re-Use and interoperability of data and computational tools using
   variant files from the DCPPC Cross-Stack Compute Demo and an annotation tool is from
   the TOPMed project. The annotations created using cost-aware cloud provisioning and the
   results are referenced by GUIDs with agreed upon metadata conventions.
*  [KC7 Controlled Access Crosscut Metadata Instance](kc7-metadata-instance.html) :
   Instructions for DCPPC Full Stacks detailing how to access the KC7 Crosscut
   Metadata Instance containing controlled-access (restricted) data. The metadata
   instance is a Team Phosphorus KC7 product. Access is provided in order to
   allow Full Stacks to ingest the metadata instance into their stacks for
   DCPPC demonstrations. Access is restricted to white-listed identities.
*  [4M.3.FULLSTACKS: Pilot Users Onboarded](globus-auth.html) : A
   description of
   [Globus Auth](https://docs.globus.org/api/auth/developer-guide/)
   and how to join the Globus Group used for authorization to data
   managed by Team Argon.
*  [4M.4.FULLSTACKS: Cross-stack Compute](cross-stack-4m.html) : A
   quickstart tutorial that walks through a quick submission of 5
   downsampled TOPMed CRAM input files using a TOPMed Alignment workflow
   in CWL. It uses a portal to index and search the input datasets and
   submits to a WES (Workflow Execution Service - GA4GH) service deployed
   as a shim-layer on the Galaxy based Globus Genomics platform.
*  [2M.1.FULLSTACKS: TopMed Workflow(s) registered on Public Site](rna-seq-pipeline.md):
   A demo describes the implementation of TOPMed RNAseq analysis
   pipeline that uses BDBags and MINID within a Galaxy based
   [Globus Genomics (GG)](http://globusgenomics.org) platform to
   support FAIR research. We have implemented specific tools within GG that
   automate the use of Minids representing input databags and generate
   output BDBags along with provenance and performance metric that can
   be used to validate reproducibility.

[back](./)
