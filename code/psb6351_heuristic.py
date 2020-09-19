import os


def create_key(template, outtype=('nii.gz',), annotation_classes=None):
    if template is None or not template:
        raise ValueError('Template must be a valid format string')
    return template, outtype, annotation_classes


def infotodict(seqinfo):
    """Heuristic evaluator for determining which runs belong where

    allowed template fields - follow python string module:

    item: index within category
    subject: participant id
    seqitem: run number during scanning
    subindex: sub index within group
    """

    data = create_key('run{item:03d}')
<<<<<<< Updated upstream

    info = {data: []}
=======
    info = {data: []}
    last_run = len(seqinfo)
>>>>>>> Stashed changes

    for s in seqinfo:
        """
        The namedtuple `s` contains the following fields:

        * total_files_till_now
        * example_dcm_file
        * series_id
        * dcm_dir_name
        * unspecified2
        * unspecified3
        * dim1
        * dim2
        * dim3
        * dim4
        * TR
        * TE
        * protocol_name
        * is_motion_corrected
        * is_derived
        * patient_id
        * study_description
        * referring_physician_name
        * series_description
<<<<<<< Updated upstream
        * sequence_name
        * image_type
        * accession_number
        * patient_age
        * patient_sex
        * date
        * series_uid

        """
=======
        * image_type
        """

>>>>>>> Stashed changes
        info[data].append(s.series_id)
    return info
