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

    #subject
    #item : each sun
    #type: fmri or dwi
    #index: ROI 1 or 2, study task: 1,2,3,4
    #dir: AP or PA

    t1w = create_key('sub-{subject}/ses-1/anat/sub-{subject}_ses-1_run-{item}_T1w')
    dwi = create_key('sub-{subject}/ses-1/dwi/sub-{subject}_ses-1_run-{item}_dwi')
    study_task =  create_key('sub-{subject}/ses-1/func/sub-{subject}_ses-1_task-study-{index}_run-{item}_bold')
    distortion = create_key('sub-{subject}/ses-1/fmap/sub-{subject}_ses-1_acq-{type}_dist_dir-{dir}_run-{item}_epi')
    roi_task = create_key('sub-{subject}/ses-1/func/sub-{subject}_ses-1_task-ROI-loc-{index}_run-{item}_bold')


    info = {t1w : [],
        dwi : [],
        study_task :  [],
        distortion : [],
        roi_task : []
        }

    last_run = len(seqinfo)

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
        * image_type
        """


        if ("T1w" in s[12]):
            info[t1w].append({"item": s.series_id})
        elif ("Study_1" in s[12]):
            info[study_task].append({"index":"1",  "item": s.series_id})
        elif ("Study_2" in s[12]):
            info[study_task].append({"index":"2",  "item": s.series_id})
        elif ("Study_3" in s[12]):
            info[study_task].append({"index":"3",  "item": s.series_id})
        elif ("Study_4" in s[12]):
            info[study_task].append({"index":"4",  "item": s.series_id})
        elif ("dMRI_AP_REVL" in s[12]):
            info[dwi].append({"item": s.series_id})
        elif ("fMRI_REVL_ROI_loc_1" in s[12]):
            info[roi_task].append({"index":"1", "item": s.series_id})
        elif ("fMRI_REVL_ROI_loc_2" in s[12]):
            info[roi_task].append({"index":"2", "item": s.series_id})
        elif ("fMRI_DistortionMap_PA" in s[12]):
            info[distortion].append({"type": "fMRI", "dir":"PA", "item": s.series_id}) 
        elif ("fMRI_DistortionMap_AP" in s[12]):
            info[distortion].append({"type": "fMRI", "dir":"AP", "item": s.series_id}) 
        elif ("dMRI_DistortionMap_PA_dMRI_REV" in s[12]):
            info[distortion].append({"type": "dwi", "dir":"PA", "item": s.series_id}) 
        elif ("dMRI_DistortionMap_AP_dMRI_REV" in s[12]):
            info[distortion].append({"type": "dwi", "dir":"AP", "item": s.series_id}) 
        else:
            pass
            
    return info
