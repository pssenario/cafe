Descripción funcional del software web para la gestión de egresados de formación titulada 

Centro de Formación: Centro Industrial y de Energías Alternativas (CIEA) — SENA Regional La Guajira 

Versión: borrador para validación con líderes de la Regional y el equipo de desarrollo 

Uso previsto: documento base para diseño funcional, modelado de datos y criterios de aceptación 

Nota de alcance del documento: este texto describe qué debe hacer el sistema y bajo qué reglas, no cómo implementarlo. Las afirmaciones sobre el marco institucional del SENA se limitan a conceptos generales y verificables (formación titulada, seguimiento a egresados, articulación con el sector productivo, bienestar del aprendiz). Todo dato, cifra, norma interna, programa o periodicidad que no pueda verificarse se marca como supuesto explícito (S-xx) o pendiente de definición (PD-xx) al final del documento, en lugar de presentarse como hecho. 

# 1. Contexto 

# 1.1 Marco institucional general 

El SENA es una entidad pública de formación profesional integral. Su oferta de formación titulada (programas técnicos, tecnológicos y especializaciones tecnológicas, entre otros) conduce a la expedición de una certificación y convierte al aprendiz en egresado. El seguimiento a egresados es una función institucional orientada a: 

medir la empleabilidad y la pertinencia de los programas frente al sector productivo de la región; 

retroalimentar el diseño curricular y la planeación de la oferta formativa del Centro; 

sostener la articulación con el sector productivo (empresas, gremios, clústeres y encadenamientos productivos del departamento); 

aportar insumos a las áreas de bienestar del aprendiz y de coordinación académica; 

alimentar los reportes institucionales que la Regional y la Dirección General requieran. 

El Centro Industrial y de Energías Alternativas (CIEA) de la Regional La Guajira atiende programas asociados a su vocación productiva, y su gestión de egresados debe reflejar esa realidad territorial, incluyendo la movilidad de los egresados dentro y fuera del departamento. 

# 1.2 Situación actual (descripción cualitativa) 

Supuesto S-01: la descripción que sigue se basa en prácticas típicas de gestión de egresados en centros de formación y debe validarse con el equipo del CIEA antes de convertirse en requisito. No se afirma que todas estas situaciones ocurran hoy en el Centro. 

De manera típica, la gestión de egresados en un centro de formación se apoya en: 

registros dispersos: hojas de cálculo, formularios diligenciados en físico o en línea, correos y mensajería instantánea, sin una fuente única de verdad; 

bases de contacto fragmentadas por programa, por ficha o por funcionario de turno; 

dependencia de personas: la información vive en el computador o la cuenta personal de quien la administra; 

seguimientos no trazables: no queda registro de quién contactó al egresado, cuándo, por qué medio ni con qué resultado; 

dificultad para consolidar indicadores de empleabilidad, pertinencia o continuidad de estudios; 

riesgo de duplicidad de registros y de pérdida de datos; 

riesgo de incumplimiento en materia de protección de datos personales (Ley 1581 de 2012 y normas concordantes), al no existir control formal de acceso y autorización. 

- 1.3 Problema que el sistema busca resolver 

El Centro no cuenta con una herramienta única, trazable y con control de acceso que permita registrar, mantener actualizada y explotar la información de los egresados de formación titulada y de su trayectoria posterior al egreso. En consecuencia: 

no hay una fuente única de verdad sobre el egresado ni sobre su situación ocupacional; 

los seguimientos no se pueden planificar, ejecutar ni verificar de forma sistemática; 

los indicadores de empleabilidad y pertinencia se construyen de forma manual, tardía y poco confiable; 

no existe trazabilidad de cambios ni control diferenciado de acceso por rol; 

la información de contacto se degrada con el tiempo sin mecanismos de actualización por parte del propio egresado. 

El sistema debe resolver: la consolidación, actualización, seguimiento y explotación controlada de la información de egresados del Centro, con trazabilidad, roles diferenciados y reportes confiables. 

1.4 Alcance del software 

Incluido en el alcance (primera versión): 

Módulo Propósito 

Autenticación y autorización Ingreso por roles, control de sesión, recuperación de acceso. Gestión de egresados Registro, consulta, actualización, inactivación y depuración de duplicados. Importación de titulados Carga masiva desde archivo estructurado proveniente de la fuente institucional (ver S-02). 

Seguimiento Registro de contactos y de la situación ocupacional/educativa del egresado, con historial. 

Novedades Registro y gestión de cambios relevantes (actualización de datos, cambio de empleo, solicitud de no contacto, etc.). 

Portal del egresado Consulta y actualización de sus propios datos de contacto y de su situación. 

Reportes e indicadores Consultas filtradas, tableros y exportación de reportes agregados y detallados. 

Auditoría Bitácora de accesos y cambios. Notificaciones Avisos internos de tareas de seguimiento y vencimientos. 

Fuera del alcance (no lo reemplaza): 

no sustituye a los sistemas institucionales de matrícula, certificación o gestión académica (p. ej., la plataforma institucional de formación), ni es fuente oficial de títulos; 

no gestiona matrícula, notas, juicios evaluativos ni etapa productiva; 

no es una bolsa de empleo ni un portal de intermediación laboral; 

no gestiona nómina, contratación ni pagos; 

no reemplaza los reportes oficiales que la Regional deba emitir por los canales definidos institucionalmente. 

# 1.5 Actores institucionales involucrados 

Actor Naturaleza Interés principal 

Administrador del sistema (rol administrativo) Funcionario del Centro designado Configurar el sistema, gestionar usuarios, aprobar novedades y cargas masivas, garantizar la calidad del dato. 

Funcionario de seguimiento a egresados (rol funcionario) Funcionario del Centro Registrar egresados, ejecutar y registrar seguimientos, gestionar novedades. 

Egresado Usuario externo Consultar y mantener actualizada su información de contacto y situación. 

Coordinador académico (rol visor)Funcionario del Centro Consultar información e indicadores para la planeación y evaluación de programas. 

Responsable de bienestar del aprendiz (rol visor) Funcionario del Centro Consultar información para acciones de acompañamiento y bienestar. 

Equipo TIC / soporte de la Regional Apoyo técnico Operación, soporte y respaldo del sistema (sin acceso a datos personales salvo lo estrictamente necesario — ver PD-01). 

Aprobación institucional del proyecto y de 

Autoridad del Centro 

Líder del Centro de Formación políticas de uso (ver PD-02). 

Entidades externas relacionadas (no usuarias del sistema): sector productivo del departamento, entidades de educación superior y la fuente institucional de datos de titulados. Su relación con el sistema se limita a la fuente de importación y al uso de reportes agregados. 

# 2. Reglas de negocio 

Formato: cada regla indica condición y consecuencia. Las reglas marcadas [PD-xx] requieren decisión institucional antes de implementarse; las marcadas [S-xx] dependen de un supuesto documentado en la sección 4. 

# 2.1 Registro y definición del egresado 

RN-01 — Origen del registro. 

Condición: un registro de egresado solo puede originarse a partir de (a) una carga masiva desde la fuente institucional de titulados, o (b) un registro manual realizado por el rol administrativo o funcionario. 

Consecuencia: el sistema no permite crear registros desde el rol egresado ni desde el rol visor. Todo registro debe conservar la referencia a su origen y a la fecha de creación. 

RN-02 — Definición de egresado titulado. 

Condición: una persona se considera egresado titulado cuando existe registro de culminación del programa de formación titulada y certificación/acta de titulación con fecha válida. 

Consecuencia: mientras no exista esa evidencia, el registro no puede marcarse como "Titulado" y no entra en los indicadores de egresados. El sistema debe almacenar la fecha de titulación y el programa asociado como datos obligatorios para el estado "Titulado". 

RN-03 — Unicidad de la persona. 

Condición: el egresado se identifica de forma unívoca por tipo y número de documento de identidad. 

Consecuencia: el sistema rechaza la creación de un segundo registro con el mismo tipo y número de documento. Si la carga masiva detecta un duplicado, lo reporta en un informe de errores y no lo inserta. 

RN-04 — Datos mínimos obligatorios. 

Condición: para guardar un egresado se requiere: tipo y número de documento, nombres y apellidos, programa de formación, número de ficha (si aplica — [S-03]), fecha de titulación, y al menos un dato de contacto vigente (correo electrónico o teléfono). 

Consecuencia: el sistema impide el guardado y señala los campos faltantes. La carga masiva rechaza las filas incompletas y las reporta. 

RN-05 — Coherencia de fechas. 

Condición: la fecha de titulación no puede ser futura ni anterior a la fecha de inicio del programa de formación. 

Consecuencia: el sistema bloquea el registro y muestra el error. Las fechas inválidas no se corrigen automáticamente. 

RN-06 — Multiplicidad de programas. 

Condición: un egresado puede tener más de un programa de formación titulada en el Centro. 

Consecuencia: el sistema permite asociar varios programas a una misma persona sin duplicar el registro de la persona, y registra el seguimiento por programa cuando el indicador así lo requiera ([S-04]). 

# 2.2 Actualización de datos 

RN-07 — Actualización por el egresado. 

Condición: el egresado autenticado puede modificar únicamente sus datos de contacto (correo, teléfonos, dirección), su situación ocupacional/educativa y sus preferencias de contacto. 

Consecuencia: el sistema registra la modificación en la bitácora con fecha, hora y usuario. Los datos académicos (programa, ficha, fecha de titulación, documento de identidad) no son editables por el egresado. 

RN-08 — Validación de contacto. 

Condición: el egresado registra o modifica un correo electrónico o teléfono. 

Consecuencia: el sistema envía una verificación al canal registrado y marca el dato como "no verificado" hasta que el egresado la confirme. Los canales no verificados no cuentan como contacto válido para efectos de seguimiento. 

RN-09 — Trazabilidad obligatoria. 

Condición: cualquier creación, modificación o inactivación de un registro. 

Consecuencia: el sistema guarda en bitácora el usuario, la fecha y hora, el valor anterior y el valor nuevo del campo modificado. La bitácora no es editable ni eliminable por ningún rol. 

RN-10 — No eliminación física. 

Condición: se requiere retirar un egresado del sistema. 

Consecuencia: el sistema solo permite inactivar el registro (con motivo obligatorio), nunca borrarlo físicamente. Los registros inactivos no aparecen en las consultas por defecto ni en los indicadores, pero permanecen consultables por el rol administrativo. 

# 2.3 Seguimiento 

RN-11 — Periodicidad mínima de seguimiento. 

Condición: todo egresado titulado debe tener al menos un seguimiento registrado dentro del período definido por el Centro ([PD-03], p. ej., semestral o anual). 

Consecuencia: el sistema genera una alerta interna para el rol funcionario cuando el egresado no tiene seguimiento dentro del período. El incumplimiento se refleja en el tablero de gestión. 

RN-12 — Contenido mínimo del seguimiento. 

Condición: se registra un seguimiento. 

Consecuencia: son obligatorios: fecha del contacto, medio utilizado (telefónico, correo, presencial, autogestionado por el egresado, otro), estado de ocupación (empleado, desempleado, estudiando, emprendimiento, otro), relación del empleo con el programa de formación (relacionado / no relacionado / no aplica), y observaciones. Si el estado es "empleado" o "emprendimiento", son obligatorios el nombre de la empresa o emprendimiento y el sector económico. Si falta alguno, el sistema no permite guardar. 

RN-13 — Autorización de tratamiento de datos. 

Condición: se va a registrar un seguimiento o actualizar datos de contacto. 

Consecuencia: el sistema exige que exista autorización vigente de tratamiento de datos personales del egresado. Si no existe o fue revocada, el sistema bloquea el registro y ofrece el mecanismo para obtenerla o registrarla. La revocatoria se trata como novedad (RN-15). 

RN-14 — Seguimiento autogestionado. 

Condición: el egresado actualiza su situación desde su portal. 

Consecuencia: el sistema crea un registro de seguimiento con medio "autogestionado" y lo deja disponible para validación del rol funcionario, sin requerir aprobación para reflejarse en los indicadores ([PD-04]). 

# 2.4 Novedades 

RN-15 — Tipos de novedad. 

Condición: ocurre un cambio relevante en la relación con el egresado. 

Consecuencia: el sistema permite registrar, como mínimo, las siguientes novedades, cada una con fecha, motivo y responsable: actualización de datos, cambio de empleo, cambio de contacto, solicitud de no ser contactado, revocatoria de autorización de datos, fallecimiento, y corrección de datos académicos. 

RN-16 — Novedad de "no contacto". 

Condición: el egresado solicita no ser contactado. 

Consecuencia: el sistema bloquea todo contacto saliente hacia ese egresado y lo excluye de las listas de gestión de seguimiento, conservando el registro histórico y los indicadores ya calculados. 

RN-17 — Novedad de corrección académica. 

Condición: se requiere corregir programa, ficha o fecha de titulación. 

Consecuencia: la novedad debe ser aprobada por el rol administrativo antes de aplicarse. Mientras no se apruebe, el dato original permanece vigente. Toda corrección aprobada queda en bitácora. 

RN-18 — Novedad de fallecimiento. 

Condición: se registra el fallecimiento de un egresado. 

Consecuencia: el sistema inactiva el registro, lo excluye de los indicadores activos y bloquea el envío de notificaciones. 

2.5 Cargas masivas 

RN-19 — Validación previa de la carga. 

Condición: el rol administrativo carga un archivo de titulados. 

Consecuencia: el sistema valida estructura, campos obligatorios, formato de fechas, tipo de documento y duplicados antes de insertar. Presenta un informe con filas aceptadas, rechazadas y su motivo. La carga solo se confirma con aprobación explícita del rol administrativo. 

RN-20 — Idempotencia de la carga. 

Condición: se carga un archivo que contiene egresados ya existentes. 

Consecuencia: el sistema actualiza los datos académicos y no duplica el registro. La actualización queda en bitácora como "actualización por carga masiva". 

2.6 Seguridad, acceso y privacidad 

RN-21 — Autenticación obligatoria. 

Condición: cualquier acceso al sistema. 

Consecuencia: se requiere autenticación previa. No existe acceso anónimo a datos personales. El egresado solo puede autenticarse si su documento coincide con un registro de egresado existente ([PD-05] sobre el mecanismo de validación de identidad). 

RN-22 — Principio de mínimo privilegio. 

Condición: un usuario ejerce una acción. 

Consecuencia: el sistema solo permite las acciones expresamente asignadas a su rol (sección 3). Cualquier acción no autorizada se rechaza y se registra en bitácora. 

RN-23 — Consulta de datos por el visor. 

Condición: el rol visor consulta información. 

Consecuencia: el visor accede a datos académicos, de seguimiento agregado e indicadores, pero no a los datos de contacto completos del egresado (correo y teléfonos se muestran enmascarados), salvo autorización expresa del rol administrativo ([PD-06]). 

RN-24 — Exportación. 

Condición: un usuario exporta información. 

Consecuencia: el rol administrativo y el funcionario pueden exportar datos detallados; el visor solo exporta reportes agregados sin identificadores personales. Toda exportación queda registrada en bitácora con usuario, fecha, filtros aplicados y número de registros. 

RN-25 — Inactividad de sesión. 

Condición: una sesión permanece inactiva por el tiempo definido por el Centro ([PD-07]). 

Consecuencia: el sistema cierra la sesión y exige autenticación nuevamente. 

# 3. Roles y permisos 

# 3.1 Resumen comparativo 

Capacidad Administrativo Funcionario Egresado Visor (Coordinador / Bienestar) Consultar listado de egresados Sí Sí No (solo su registro) Sí Ver datos de contacto completos Sí Sí Solo los propios No (enmascarados) Crear egresado manualmente Sí Sí No No Cargar archivo masivo Sí No No No Editar datos académicos Sí (con aprobación de novedad) No No No Editar datos de contacto Sí Sí Solo los propios No Registrar seguimiento Sí Sí Autogestionado No Validar seguimiento autogestionado Sí Sí No No Aprobar novedades Sí No No No Inactivar egresado Sí No No No Gestionar usuarios y roles Sí No No No Consultar indicadores y tableros Sí Sí No Sí Exportar datos detallados Sí Sí No No Exportar reportes agregados Sí Sí No Sí Consultar bitácora de auditoría Sí No No No 3.2 Rol administrativo 

Puede: 

configurar parámetros del sistema (periodicidad de seguimiento, catálogos, medios de contacto); 

crear, consultar, actualizar e inactivar egresados; 

ejecutar y aprobar cargas masivas; 

aprobar novedades, incluidas las correcciones académicas (RN-17); 

aprobar la creación de usuarios y la asignación de roles; 

consultar la bitácora de auditoría; 

exportar datos detallados y agregados; 

autorizar, de forma expresa y registrada, el acceso temporal del visor a datos de contacto ([PD-06]). 

Restringido: 

no puede eliminar físicamente registros (RN-10); 

no puede modificar ni borrar la bitácora; 

no puede alterar la fecha de titulación sin que quede como novedad aprobada y registrada; 

no puede otorgarse a sí mismo permisos que no le correspondan por política del Centro. 

3.3 Rol funcionario 

Puede: 

consultar egresados de los programas que tenga asignados ([PD-08] sobre si la asignación es por programa o global); 

crear egresados manualmente y actualizar sus datos de contacto; 

registrar seguimientos y adjuntar evidencias; 

validar seguimientos autogestionados; 

registrar novedades (quedan pendientes de aprobación cuando la regla lo exija); 

generar y exportar reportes detallados de su ámbito de gestión; 

recibir alertas de seguimiento vencido. 

Restringido: 

no puede aprobar novedades ni cargas masivas; 

no puede inactivar egresados; 

no puede modificar datos académicos; 

no puede gestionar usuarios ni roles; 

no puede consultar la bitácora de auditoría. 

3.4 Rol egresado 

Puede: 

autenticarse y consultar su propio registro; 

actualizar sus datos de contacto y su situación ocupacional/educativa; 

registrar o revocar la autorización de tratamiento de datos; 

solicitar la novedad de "no contacto"; 

consultar el historial de sus propios seguimientos. 

Restringido: 

no puede consultar información de otros egresados; 

no puede modificar datos académicos (programa, ficha, fecha de titulación, documento); 

no puede crear ni aprobar novedades distintas de las propias; 

no puede exportar información ni acceder a indicadores globales. 

3.5 Rol visor (Coordinador académico y Responsable de bienestar del aprendiz) 

Puede: 

consultar el listado de egresados y sus datos académicos y de seguimiento; 

aplicar filtros por programa, ficha, período de titulación, estado de ocupación y sector económico; 

consultar tableros e indicadores agregados (empleabilidad, pertinencia, continuidad de estudios, distribución por sector); 

exportar reportes agregados sin identificadores personales; 

consultar el detalle de un egresado viendo sus datos de contacto enmascarados (RN-23). 

Restringido: 

no puede crear, modificar ni inactivar egresados; 

no puede registrar seguimientos ni validar los autogestionados; 

no puede registrar ni aprobar novedades; 

no puede cargar archivos masivos; 

no puede ver datos de contacto completos ni exportar datos personales detallados; 

no puede gestionar usuarios ni consultar la bitácora. 

3.6 Diferencias explícitas entre visor y funcionario Dimensión Funcionario Visor Naturaleza del acceso Operativo: ejecuta el proceso de seguimiento Consulta: observa y analiza Creación y edición de registros Sí No Registro de seguimiento Sí No Aprobaciones No (solo el administrativo aprueba) No Datos de contacto Completos Enmascarados Exportación Detallada, con datos personales Solo agregada, sin identificadores Alertas de tareas Sí, recibe y gestiona No recibe tareas de seguimiento Ámbito Programas asignados Todos los programas del Centro ([PD-09]) 

Nota: si el Responsable de bienestar del aprendiz requiere datos de contacto para acciones de acompañamiento, se debe definir una autorización temporal y registrada (RN-23 / PD-06). Esta es una decisión institucional, no una decisión técnica. 

4. Supuestos explícitos y pendientes de definición 

4.1 Supuestos 

S-01. La descripción de la situación actual (1.2) es una hipótesis de trabajo a validar con el CIEA. 

S-02. Existe una fuente institucional oficial con el listado de titulados que el sistema podrá consumir mediante archivo estructurado (CSV/XLSX) en la primera fase; la integración en tiempo real queda para una fase posterior. 

S-03. El número de ficha es un dato disponible y relevante para la operación del Centro; si no lo es, se tratará como opcional. 

S-04. Un egresado puede acumular varios programas de formación titulada en el Centro y el seguimiento se asocia al egresado, no al programa, salvo que el indicador requiera desagregación. 

S-05. El sistema operará en español y con conectividad a internet, dado el contexto de la Regional. 

S-06. La gestión de identidad del egresado se resolverá con validación contra el registro de egresados del propio sistema en la primera fase. 

S-07. El sistema no sustituye a los sistemas institucionales de matrícula y certificación; el dato oficial de titulación proviene de ellos. 

4.2 Pendientes de definición 

PD-01. Nivel de acceso del equipo TIC de la Regional a datos personales y a la bitácora. 

PD-02. Instancia que aprueba formalmente las políticas de uso, retención y acceso del sistema. 

PD-03. Periodicidad oficial del seguimiento a egresados del Centro. 

PD-04. Si el seguimiento autogestionado por el egresado requiere validación del funcionario para reflejarse en los indicadores. 

PD-05. Mecanismo de validación de identidad del egresado para autenticarse (documento + fecha de nacimiento, código de verificación, correo institucional u otro). 

PD-06. Autorización temporal y registrada para que el visor (bienestar) acceda a datos de contacto, con su alcance y duración. 

PD-07. Tiempo de inactividad de sesión y política de contraseñas. 

PD-08. Si el ámbito del funcionario es por programa, por ficha o global. 

PD-09. Si el visor consulta todos los programas del Centro o solo los de su área. 

PD-10. Política de retención de datos y de depuración de registros inactivos. 

PD-11. Indicadores oficiales y su fórmula de cálculo (empleabilidad, pertinencia, continuidad de estudios), que deben definirse con la coordinación académica antes del diseño de los tableros. 

