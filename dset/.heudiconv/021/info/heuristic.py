import os


def create_key(template, outtype=('nii.gz',), annotation_classes=None):
    if template is None or not template:
        raise ValueError('Template must be a valid format string')
    return template, outtype, annotation_classes


def infotodict(seqinfo):

    t1w = create_key('C:/Users/Patricio Viera/Documents/GitHub/mattfeld_2020/dset/sub-{subject}/anat/sub-{subject}_T1w')
    dwi = create_key('C:/Users/Patricio Viera/Documents/GitHub/mattfeld_2020/dset/sub-{subject}/anat/sub-{subject}_run-{item:01d}_dwi')
    func = create_key('C:/Users/Patricio Viera/Documents/GitHub/mattfeld_2020/dset/sub-{subject}/anat/sub-{subject}_task-REVL_rec-{rec}_run-{item:01d}_bold')

    info = {t1w: [], dwi: [], func: []}

    for s in seqinfo:#each row of dicominfo.tsv
        if (s.dim1 == 256) and (s.dim2 == 256) and (s.dim3 == 176) and (s.dim4 == 1) and ('T1w' in s.protocol_name):
            info[t1w] = [s.series_id] #This appends to t1w folder if scans meet criteria
        if (s.dim1 == 140) and (s.dim2 == 140) and (s.dim3 == 81) and (s.dim4 == 103) and ('dMRI' in s.protocol_name):
            info[dwi] = [s.series_id] #Appends to the dwi folder
        if (s.dim1 == 100) and (s.dim2 == 100) and (s.dim3 == 66) and (s.dim4 ==355) and ('fMRI' in s.protocol_name): #Appends to the func folder
            if ('Study_1' in s.protocol_name): #Separates by Study
                info[func].append({'item': s.series_id, 'rec': 'Study_1'})
            if ('Study_2' in s.protocol_name)('Study_1' in s.protocol_name):
                info[func].append({'item': s.series_id, 'rec': 'Study_2'})
            if ('Study_3' in s.protocol_name):
                info[func].append({'item': s.series_id, 'rec': 'Study_3'})
            else:
                info[func].append({'item': s.series_id, 'rec': 'Study_4'})
    return info
