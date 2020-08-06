# acpiparse

acpiparse is a small utility which understands the format of common
ACPI tables and can print them in a human-readable way.

This is primarily meant for quickly understanding the ACPI configuration
of a machine and understanding kernel behavior.

On most Linux systems, you can get the ACPI tables from
`/sys/firmware/acpi/tables`.

## Currently supported tables

* TPM2
* APIC (header only for now)

## Coming soon

* APIC (remaining fields)
* FACP
* FACS

