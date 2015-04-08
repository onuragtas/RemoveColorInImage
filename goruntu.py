#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  goruntu.py
#  
#  Copyright 2015 Onur Ağtaş <onuragtas@Linux>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import os, sys
import Image
picture = sys.argv[1];
print picture;
im = Image.open(picture)
width, height = im.size
pix = im.load()
dr,dg,db = pix[1,1]
for w in range(0, width):
	for h in range(0, height):

		pix = im.load()
		r,g,b = pix[w,h]
		
		if (r<=255 and r>=188) or (g<=239 and g>=188) or (b<=253 and b>=188):
			print w,h,r,g,b;
			im.putpixel( (w,h), (255,255,255))	
im.save("1"+picture);
