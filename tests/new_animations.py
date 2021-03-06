from manimlib.imports import *

# python -m manim ejemplos_animaciones_nuevas_tb.py

class SeleccionTexto(Scene):
    CONFIG = {"include_sound": True}
    def construct(self):
        texto=TextMobject("Texto",color=WHITE).scale(3)
        self.play(Escribe(texto,rate_func=linear))
        seleccion_texto(self,texto)
        self.play(mostrar_seleccion_texto(self,texto))
        self.wait()
        self.play(texto.rect.fade,1)
        self.wait()

class SeleccionTextoGrande(Scene):
    def construct(self):
        texto1=TextMobject("Texto 1",color=WHITE).scale(3)
        texto2=TextMobject("Texto 2",color=WHITE).scale(3)
        VGroup(texto1,texto2).arrange_submobjects(DOWN,buff=0.5)
        self.play(Escribe(texto1),Escribe(texto2))
        seleccion=seleccion_grande_texto(self,texto1)
        self.play(FadeIn(seleccion))
        mueve_seleccion(self,seleccion,texto2)
        self.wait()
        mueve_seleccion(self,seleccion,texto1)
        self.wait()

class RemplazoTexto(Scene):
    def construct(self):
        texto=Texto("Teoría de la gravedadñé").to_corner(UL)
        texto2=Texto("Contradicción con la ciencia")
        texto3=Texto("Eso no es verdad")
        
        texto=escribe_texto(self,texto)
        self.wait()
        texto2=reescribe_texto(self,texto,texto2)
        self.wait()
        texto3=reescribe_texto(self,texto2,texto3)
        self.play(texto3.shift,RIGHT)
        self.play(texto3[2].set_color,RED)
        self.wait(2)

class GrillaEscena(Scene):
    def construct(self):
        grilla=Grilla()
        p1=Dot(coord(3.05,-1))
        p2=Dot(coord(-2,3))
        flecha1=DVFlecha(p1.get_center(),p2.get_center())
        self.add(grilla,p1,p2,flecha1)
        self.wait()

class Dimensiones2(Scene):
    def construct(self):
        rectangulo=Rectangle(width=5,height=3)
        rectangulo.rotate(30*DEGREES)
        linea=Line(LEFT*1.5,RIGHT*1.5)
        linea.rotate(20*DEGREES)
        linea.shift(LEFT*2)
        v_medicion=Medicion(linea).add_tips().add_letter("x",buff=2)
        self.play(ShowCreation(linea))
        self.play(GrowFromCenter(v_medicion))
        def update(grupo):
            nueva_medicion=Medicion(linea).add_tips().add_letter("x",buff=2)
            for i in range(len(grupo)-1):
                grupo[i].put_start_and_end_on(nueva_medicion[i].get_start(),nueva_medicion[i].get_end())
            grupo[-1].move_to(nueva_medicion[-1])


        self.play(linea.scale,2,linea.rotate,PI/8,linea.shift,RIGHT*3,
            UpdateFromFunc(
            v_medicion,update))
        self.wait(2)

class Teclado(Scene):
    CONFIG = {"include_sound": True,
    "camera_config":{"background_color":FONDO_ST}}
    def construct(self):
        self.wait()
        texto=TikzMobject("""
\\begin{lstlisting}[language=Python,style=basic,numbers=none]
<contenido>
    <tema1>
    Tema 1
        <tema1.1>
            Subtema 1
        </tema1.1>
    </tema1>
    <tema2> 
    Tema 2 
        <tema2.1>
            Subtema 2
        </tema2.1>
    </tema2>
</contenido>
\\end{lstlisting}
            """).set_stroke(None,0).set_fill(WHITE,0).scale(2).to_corner(UL)
        for i in list(range(0,11))+list(range(105,117)):
            texto[i].set_color(ROSA_ST)
        for i in list(range(11,18))+list(range(50,65))+list(range(97,105)):
            texto[i].set_color(VERDE_ST)
        for i in list(range(23,32))+list(range(40,50))+list(range(70,79))+list(range(87,97)):
            texto[i].set_color(AMARILLO_ST)
        self.add(texto)
        #'''
        KeyBoard(self,texto[0:40],p=0.037,time_random=0.037)
        self.wait()
        self.play(texto.move_to,np.array([0,2,0])+texto.get_center())
        KeyBoard(self,texto[40:87],p=0.037,time_random=0.037)
        self.wait()
        self.play(texto.move_to,np.array([0,4,0])+texto.get_center())
        KeyBoard(self,texto[87:],p=0.037,time_random=0.037)
        #'''
        #self.play(texto.move_to,np.array([0,2,0])+texto.get_center())

class Soporte(Scene):
    def construct(self):
        pat1=Patron(width=4,height=7,grosor=0.5,agregar_base=True,direccion="R",stroke_width=5)
        pat1[-1].scale(1.007).shift(RIGHT*0.02)
        pat2=Patron(width=2,height=7,grosor=0.5,agregar_base=True,direccion="R",stroke_width=5)
        pat2[-1].scale(1.007).shift(RIGHT*0.02)
        pat1.shift(LEFT*4)
        pat2.shift(LEFT*4)
        self.play(*[LaggedStart(ShowCreation,pat1[i],rate_func=linear)for i in range(len(pat1))])
        self.play(Transform(pat1,pat2))
        self.wait()

class Indice(EscenaContenido):
    CONFIG={
    "escala":0.7
    }
    def setup(self):
        self.contenido=[
            "Tema de lo que \\\\ sea - (6:20)",
                "Sub tema",
                "Sub tema",
            "--",
            "Tema - (6:12)",
                "Sub tema",
                "Sub tema",
            "--",
            "Tema",
                "Sub tema",
                "Sub tema",
                "Sub tema",
            "--",
            "Tema",
                "Sub tema",
            "--",]


class ObjetoCaja(Scene):
    def construct(self):
        objeto=Caja(ancho=4)
        cinta=Nota1()
        cinta.move_to(objeto)
        objeto_etiqueta=Formula("A",color=BLACK).move_to(objeto)
        cinta.set_height(objeto_etiqueta.get_height()*2)
        self.play(ShowCreation(objeto))
        self.play(objeto.set_fill,None,0.85)

        def update(imagen):
            imagen.move_to(objeto_etiqueta)
            return imagen
        self.play(FadeInFrom(cinta,UP))
        self.wait()

        self.play(Escribe(objeto_etiqueta))
        objeto.add(objeto_etiqueta)
        self.play(objeto.shift,DOWN*3+LEFT*2,UpdateFromFunc(cinta,update),path_arc=PI/4)
        self.wait()
        self.play(objeto_etiqueta.move_to,objeto.get_corner(UL),objeto_etiqueta.shift,cinta.get_width()*RIGHT*1.3/2+cinta.get_height()*DOWN*1.3/2,UpdateFromFunc(cinta,update))
        self.play(abrir_caja(objeto))

        self.play(objeto.shift,UP*4.5+RIGHT*4,UpdateFromFunc(cinta,update),path_arc=PI/4)
        self.wait()
        self.play(cerrar_caja(objeto))
        self.wait()

class Titulo(Scene):
    def construct(self):
        tikz="""
            \\begin{tikzpicture}[pencildraw/.style={decorate,
            decoration={random steps,segment length=0.8pt,amplitude=0.3pt}}]
                \\node[pencildraw,draw] {\\sc Derivada};
            \\end{tikzpicture} 
              """
        tit=TextFull(tikz,stroke_width=2,fill_opacity=.1).scale(3)
        tit[1:].set_stroke(None,0).set_fill(WHITE,1)
        self.play(Write(tit),run_time=3)
        self.wait()

class OmegaDice(Scene):
    def construct(self):
        Ale=Alex()
        palabras_ale = TextMobject("Yo soy OmegaCreature")
        self.play(FadeIn(Ale.to_edge(DL)))
        self.play(Blink(Ale))
        self.play(OmegaCreatureDice(
            Ale, palabras_ale, 
            bubble_kwargs = {"height" : 3, "width" : 4},
            target_mode="speaking"
        ))
        self.wait()
        self.play(Blink(Ale))
        self.play(RemueveDialogo(Ale))
        self.play(
            Ale.change_mode, "participa"
        )
        self.play(OmegaCreatureDice(
            Ale, palabras_ale, 
            bubble_kwargs = {"height" : 3, "width" : 4},
            target_mode="participa"
        ))
        self.wait()
        self.play(Blink(Ale))
        self.play(RemueveDialogo(Ale))       
        self.play(FadeOut(Ale))
        self.wait(0.5)

class Conversacion(Scene):
    def construct(self):
        conversation = Conversation(self)
        conversation.add_bubble("Hola!")
        self.wait(2)
        conversation.add_bubble("Hola, qué tal?")
        self.wait(2)
        conversation.add_bubble("Esta es mi primera animación de\\\\ conversación.")
        self.wait(3) # 41
        conversation.add_bubble("Está muy bien!")
        self.wait(2) # 48
        conversation.add_bubble("Gracias! :D")
        self.wait(2)
        self.play(FadeOut(conversation.dialog[:]))
        self.wait()

class EscenaMusica(MusicalScene):
    def construct(self):
        self.teclado_transparente=self.definir_teclado(4,self.prop,0).set_stroke(None,0)
        self.teclado_base=self.definir_teclado(4,self.prop,0)
        self.teclado_base.move_to(ORIGIN+DOWN*3)
        self.teclado_transparente.move_to(ORIGIN+DOWN*3)

        self.wait(0.3)
        self.agregar_escenario()
        self.mandar_frente_sostenido(4,self.teclado_base)
        self.mandar_frente_sostenido(4,self.teclado_transparente)

        self.primer_paso(simbolos_faltantes=[14,15,16,17,18,19,20,21])
        self.progresion(0,run_time=2)
        self.progresion_con_desfase(paso=1,desfase=22,y1=8,x2=8,y2=16,run_time=2)
        self.progresion_con_desfase(paso=2,desfase=30,y1=8,x2=10,y2=18,simbolos_faltantes=[38,39],run_time=2)

        self.intervalos()

        self.salida_teclado()
        
        self.wait(2)


    def importar_partitura(self):
        self.partitura=TextMobject("""
                \\begin{music}
                \\parindent10mm
                \\instrumentnumber{1}
                \\setname1{} 
                \\setstaffs1{2}
                \\setclef16
                \\startextract
                \\NOTEs\\zql{'C}\\qu G|\\zql{e}\\qu j\\en
                \\NOTEs\\zql{F}\\qu{''A}|\\zql{f}\\qu{'c}\\en
                \\NOTEs\\zql{G}\\qu{'G}|\\zql{d}\\qu{'b}\\en
                \\NOTEs\\zhl{C}\\hu{'G}|\\zhl{e}\\hu{'c}\\en
                \\endextract
                \\end{music}
            """,color=BLACK).shift(UP)

    def definir_cambios_notas(self):
        self.cambios_notas=[[[
                (   14, 15, 17, 16, 18, 19, 21, 20, ),
                (   22, 23, 25, 24, 26, 27, 29, 28, )
        ]]]

        self.teclas=[[29,37,28,36],
                    [30,35,29,36],
                    [27,36,26,35],
                    [1,20,28,36]]

    def definir_colores(self):
        
        self.colores_notas=[
                       ([21,20,29,28,36,37,47,46],self.colores[3]),
                       ([18,19,26,27,34,35,44,45],self.colores[2]),
                       ([17,16,25,24,33,32,43,42],self.colores[1]),
                       ([14,15,22,23,30,31,40,41,38,39],self.colores[0])
                      ]


    def definir_cifrado(self):
        cifrado=VGroup(
            TexMobject("\\mbox{I}_3^6",color=BLACK),
            TexMobject("\\mbox{IV}_3^4",color=BLACK),
            TexMobject("\\mbox{V}",color=BLACK),
            TexMobject("\\mbox{I}",color=BLACK)
            )
        bajo=[15,23,31,41]
        cifrado[0].next_to(self.partitura[15],DOWN,buff=1.3)
        cords_x=[*[self.partitura[w].get_center()[0]for w in bajo]]
        
        for i in range(1,4):
            cifrado[i].move_to(cifrado[i-1])
            dis=cords_x[i]-cords_x[i-1]
            cifrado[i].shift(np.array([dis,0,0]))

        self.cifrado=cifrado        

    def agregar_escenario(self):
        self.grupoA=VGroup(*[self.partitura[cont]for cont in [12,13]])
       
        self.play(*[LaggedStart(GrowFromCenter, self.partitura[i],run_time=2)for i in range(1,11)],
            LaggedStart(DrawBorderThenFill,self.teclado_transparente),LaggedStart(DrawBorderThenFill,self.teclado_base)
            )
        self.play(*[GrowFromCenter(x)for x in self.grupoA])



    def intervalos(self):
        i6m_v=self.intervalo_v(21,15,"6-")
        i5J_v=self.intervalo_v(25,29,"5\\rm J",direccion=RIGHT)

        i2m_h=self.intervalo_h(17,25,"2+")
        i5J_h=self.intervalo_h(15,23,"5\\rm J")

        self.ap_inter_v(i6m_v)
        self.wait()
        self.play(ReplacementTransform(i6m_v.copy(),i5J_v))
        self.wait()
        self.ap_inter_h(i2m_h)
        self.wait()
        self.play(ReplacementTransform(i2m_h,i5J_h))
        self.wait()
        
    def salida_teclado(self):
        self.play(*[
                ApplyMethod(
                    self.teclado_transparente[i].set_fill,None,0
                    )
                for i,color in self.cambios_colores_teclas[3]
                ],
            run_time=1
        )
        for i in range(len(self.teclado_transparente)):
            self.remove(self.teclado_transparente[i])
        for i in range(len(self.teclado_base)):
            self.remove(self.teclado_base[i])
        self.play(
            LaggedStart(FadeOutAndShiftDown,self.teclado_base,lambda m: (m, DOWN),run_time=1),
            LaggedStart(FadeOutAndShiftDown,self.teclado_transparente,lambda m: (m, DOWN),run_time=1)
            )

class Escala2(MusicalScene): #Usar MuscalScene2
    def setup(self):
        self.definir_teclados(1,ORIGIN,0.6)
        self.definir_teclas(1)

    def construct(self):
        self.agregar_escenario()
        self.mover_teclas()
        self.copiar_teclado()
        self.wait()
        #self.mostrar_notas(self.teclado_base)


    def agregar_escenario(self):
        #self.linea=Line(self.teclado_transparente[0].get_top(),self.teclado_transparente[-1].get_top()).set_stroke(BLACK,width=1.5)
        self.play(
            LaggedStart(FadeInFromDown,self.teclado_base)
            )
        self.wait()
        #self.play(FadeIn(self.linea))

    def mover_teclas(self):
        self.teclado_base2=self.teclado_base.copy()
        for i in range(1,len(self.teclado_base2)):
            self.teclado_base2[i].next_to(self.teclado_base2[i-1],RIGHT,buff=0)
        self.teclado_base2.move_to(ORIGIN)

        self.play(ReplacementTransform(self.teclado_base,self.teclado_base2),run_time=3.4)
        self.teclado_base3=self.teclado_base2.copy()
        self.wait()

        self.teclado_base3.move_to(np.array([0,-1.65,0]))
        for i in range(1,len(self.teclado_base3)):
            if i in [1,3,6,8,10]:
                self.teclado_base3[i].shift(UP*abs(self.teclado_base3[i].get_height()-self.teclado_base3[i-1].get_height())/2+UP*0.3*i)
            else:
                self.teclado_base3[i].shift(UP*0.3*i)

        self.play(ReplacementTransform(self.teclado_base2,self.teclado_base3),run_time=3)
        self.teclado_base=self.teclado_base3
        
        #self.teclado_base.move_to(ORIGIN)
        #self.add(Texto("%f\\\\%f"%(self.teclado_base[0].get_center()[0],self.teclado_base[0].get_center()[1]),color=RED))

    def copiar_teclado(self):
        self.play(self.teclado_base.scale,0.5)
        self.teclado_superior1=self.teclado_base.copy()
        self.teclado_superior1.next_to(self.teclado_base,RIGHT,buff=0).shift(UP*(self.teclado_base.get_height()/2+0.2))
        self.teclado_inferior1=self.teclado_base.copy()
        self.teclado_inferior1.next_to(self.teclado_base,LEFT,buff=0).shift(DOWN*(self.teclado_base.get_height()/2+0.2))
        self.play(ReplacementTransform(self.teclado_base.copy(),self.teclado_superior1,path_arc=PI),
            ReplacementTransform(self.teclado_base.copy(),self.teclado_inferior1,path_arc=PI),run_time=2.5)
        self.teclado_superior2=self.teclado_superior1.copy()
        self.teclado_inferior2=self.teclado_inferior1.copy()
        self.teclado_superior2.next_to(self.teclado_superior1,RIGHT,buff=0).shift(UP*(self.teclado_base.get_height()/2+0.2))
        self.teclado_inferior2.next_to(self.teclado_inferior1,LEFT,buff=0).shift(DOWN*(self.teclado_base.get_height()/2+0.2))
        self.play(ReplacementTransform(self.teclado_inferior1.copy(),self.teclado_inferior2,path_arc=PI),
            ReplacementTransform(self.teclado_superior1.copy(),self.teclado_superior2,path_arc=PI),run_time=2.5)

        self.teclado_superior3=self.teclado_superior2.copy()
        self.teclado_inferior3=self.teclado_inferior2.copy()
        self.teclado_superior3.next_to(self.teclado_superior2,RIGHT,buff=0).shift(UP*(self.teclado_base.get_height()/2+0.2))
        self.teclado_inferior3.next_to(self.teclado_inferior2,LEFT,buff=0).shift(DOWN*(self.teclado_base.get_height()/2+0.2))
        self.play(ReplacementTransform(self.teclado_inferior2.copy(),self.teclado_inferior3,path_arc=PI),
            ReplacementTransform(self.teclado_superior2.copy(),self.teclado_superior3,path_arc=PI),run_time=2.5)


        self.teclado_superior4=self.teclado_superior3.copy()
        self.teclado_inferior4=self.teclado_inferior3.copy()
        self.teclado_superior4.next_to(self.teclado_superior3,RIGHT,buff=0).shift(UP*(self.teclado_base.get_height()/2+0.2))
        self.teclado_inferior4.next_to(self.teclado_inferior3,LEFT,buff=0).shift(DOWN*(self.teclado_base.get_height()/2+0.2))
        self.play(ReplacementTransform(self.teclado_inferior3.copy(),self.teclado_inferior4,path_arc=PI),
            ReplacementTransform(self.teclado_superior3.copy(),self.teclado_superior4,path_arc=PI),run_time=2.5)

        self.teclado_escala=VGroup(self.teclado_base,
            self.teclado_superior1,
            self.teclado_superior2,
            self.teclado_superior3,
            self.teclado_superior4,
            self.teclado_inferior1,
            self.teclado_inferior2,
            self.teclado_inferior3,
            self.teclado_inferior4)

        self.play(self.teclado_escala.shift,np.array([2,1.8,0]),rate_func=there_and_back,run_time=3)
        self.play(self.teclado_escala.shift,np.array([-2,-1.8,0]),rate_func=there_and_back,run_time=3)




        self.teclado_3octavas=self.definir_octava_back(9).move_to(ORIGIN).scale(0.4)
        self.wait()

        
        self.play(
            *[ReplacementTransform(self.teclado_inferior4[i4],self.teclado_3octavas[i4])for i4 in range(len(self.teclado_inferior1))],
            *[ReplacementTransform(self.teclado_inferior3[i3],self.teclado_3octavas[i3+12])for i3 in range(len(self.teclado_inferior1))],
            *[ReplacementTransform(self.teclado_inferior2[i2],self.teclado_3octavas[i2+24])for i2 in range(len(self.teclado_inferior1))],
            *[ReplacementTransform(self.teclado_inferior1[i1],self.teclado_3octavas[i1+36])for i1 in range(len(self.teclado_inferior1))],
            *[ReplacementTransform(self.teclado_base[j],self.teclado_3octavas[j+48])for j in range(len(self.teclado_base))],
            *[ReplacementTransform(self.teclado_superior1[k1],self.teclado_3octavas[k1+60])for k1 in range(len(self.teclado_superior1))],
            *[ReplacementTransform(self.teclado_superior2[k2],self.teclado_3octavas[k2+72])for k2 in range(len(self.teclado_superior1))],
            *[ReplacementTransform(self.teclado_superior3[k3],self.teclado_3octavas[k3+84])for k3 in range(len(self.teclado_superior1))],
            *[ReplacementTransform(self.teclado_superior4[k4],self.teclado_3octavas[k4+96])for k4 in range(len(self.teclado_superior1))])
            #'''

        self.play(self.teclado_3octavas.shift,LEFT*3,rate_func=there_and_back,run_time=3)
        self.play(self.teclado_3octavas.shift,RIGHT*3,rate_func=there_and_back,run_time=3)

class ZoomedSceneExample(ZoomedScene):
    CONFIG = {
        "zoom_factor": 0.5,
        "zoomed_display_height": 1,
        "zoomed_display_width": 6,
        "image_frame_stroke_width": 20,
        "zoomed_camera_config": {
            "default_frame_stroke_width": 3,
        },
    }

    def construct(self):
        # Set objects
        dot = Dot().shift(UL*2)
        frame_rate = self.camera.frame_rate
        image=NumberPlane()

        frame_text=TextMobject("Frame",color=PURPLE).scale(1.4)
        zoomed_camera_text=TextMobject("Zommed camera",color=RED).scale(1.4)

        self.add(image,dot)

        # Set camera
        zoomed_camera = self.zoomed_camera
        zoomed_camera.cairo_line_width_multiple = 0.05
        zoomed_display = self.zoomed_display
        frame = zoomed_camera.frame
        zoomed_display_frame = zoomed_display.display_frame

        frame.move_to(dot)
        frame.set_color(PURPLE)

        zoomed_display_frame.set_color(RED)
        zoomed_display.shift(DOWN)

        # brackground zoomed_display
        zd_rect = BackgroundRectangle(
            zoomed_display,
            fill_opacity=0,
            buff=MED_SMALL_BUFF,
        )

        self.add_foreground_mobject(zd_rect)

        # animation of unfold camera
        unfold_camera = UpdateFromFunc(
            zd_rect,
            lambda rect: rect.replace(zoomed_display)
        )

        frame_text.next_to(frame,DOWN)

        self.play(
            ShowCreation(frame),
            FadeInFromDown(frame_text)
        )

        # Activate zooming
        self.activate_zooming()

        self.play(
            # You have to add this line
            self.get_zoomed_display_pop_out_animation(),
            unfold_camera
        )

        zoomed_camera_text.next_to(zoomed_display_frame,DOWN)
        self.play(FadeInFromDown(zoomed_camera_text))

        # Scale in     x   y  z
        scale_factor=[0.5,1.5,0]
        self.change_cairo(0.07)


        # Resize the frame and zoomed camera
        self.play(
            frame.scale,                scale_factor,
            zoomed_display.scale,       scale_factor,
            FadeOut(zoomed_camera_text),
            FadeOut(frame_text)
        )

        # Resize the frame
        self.play(
            frame.scale,3,
            frame.shift,2.5*DOWN
        )

        # Resize zoomed camera
        self.play(
            ScaleInPlace(zoomed_display,2)
        )


        self.wait()

        self.change_cairo(0.3)

        self.play(
            self.get_zoomed_display_pop_out_animation(),
            unfold_camera,
            # -------> Inverse
            rate_func=lambda t: smooth(1-t),
        )
        

        self.play(
            Uncreate(zoomed_display_frame),
            FadeOut(frame),
            FadeOut(zoomed_display)
        )
        self.wait()

    def change_cairo(self,val_end):
        frame_rate = self.camera.frame_rate
        start_cairo = self.zoomed_camera.cairo_line_width_multiple
        d_cairo = val_end
        ds = abs(start_cairo - d_cairo) / frame_rate
        print(start_cairo)
        print(abs(start_cairo - d_cairo))

        for i in range(frame_rate):
            if start_cairo>d_cairo:
                self.zoomed_camera.cairo_line_width_multiple -= ds
            else:
                self.zoomed_camera.cairo_line_width_multiple += ds
            self.wait(1/frame_rate)

        print(self.zoomed_camera.cairo_line_width_multiple)

class CompassScene(Scene):
    def construct(self):
        #self.show_compass()
        #self.simple_animation()
        self.test_animation_1()
        
    def show_compass(self):
        compas = Compas()
        self.add(compas)
        
    def simple_animation(self):
        arc = PI*2
        compass = Compass()
        compass2 = Compass(gap=3,stroke_material=0.4)
        dot = Dot(radius=0.05)

        self.play(GrowFromCenter(dot))
        self.add_foreground_mobject(compass)

        self.play(FadeInFrom(compass,UP))
        self.play(
            *compass.Rotate(arc,needle="B",arc_color=BLUE),
            run_time=3
            )
        self.play(OpenCompass(compass,3))
        self.play(
            *compass.Rotate(PI/2),
            run_time=3
            )
        print(compass.get_angle())
        self.play(
            *compass2.Rotate(PI,needle="B"),
            run_time=3
            )
        self.play(compass.draws[0].set_color,PINK)
        #self.play(compass.draws[1].set_color,YELLOW)
        #self.play(compass.draws[2].set_color,PURPLE)
        self.wait()

    def test_animation_1(self):
        compass = Compass(gap=1.5)
        compass.shift(LEFT*(2.5/2))
        title = Text("Bisection").to_edge(UP)
        angle = 0.7*PI/4
        self.play(Write(title))
        self.play(title.fade,0.5)
        self.play(ShowCreation(Line(LEFT*2.5/2,RIGHT*2.5/2)))
        self.play(FadeInFrom(compass,UP))
        self.add_foreground_mobject(compass)

        self.write_segment(compass,angle)
        self.write_segment(compass,-angle)
        self.play(PositionCompass(compass,0))
        self.play(compass.shift,RIGHT*(2.5-1.5))
        self.write_segment(compass,angle,needle="B")
        self.write_segment(compass,-angle,needle="B")
        self.play(PositionCompass(compass,0,needle="B"))
        self.play(FadeOut(compass))

        self.wait()

    def write_segment(self,compass,angulo,arco=20*DEGREES,needle="A"):
        if needle=="A":
            target_angle=angulo-arco/2
        if needle=="B":
            target_angle=angulo+arco/2
        self.play(PositionCompass(compass,target_angle,needle=needle))
        self.play(*compass.Rotate(arco,needle=needle),run_time=1)

class Lines(Scene):
    def construct(self):
        dot = Dot(color=RED)
        lines_group = VGroup(Line(LEFT,RIGHT))
        def update_lines(mob):
            new_line = Line(dot.get_center()+LEFT,dot.get_center()+RIGHT)
            new_mob = mob.copy()
            new_mob.add(new_line)
            mob.become(new_mob)

        self.add(dot,lines_group)
        self.add_foreground_mobjects(dot)
        self.play(
                dot.shift,UP*2,
                UpdateFromFunc(lines_group,update_lines)
                )
        self.wait()

class Test2(Scene):
    def construct(self):
        text = FunText(r"Alexander").scale(3)
        draw = FreehandRectangle(text,margin=0.2,partitions=30,color=RED,fill_opacity=0.3)
        self.play(DrawBorderThenFill(draw),FadeInFromEdges(text[0]))
        self.wait()

class Test3(Scene):
    def construct(self):
        text = FunText(r"Alexander").scale(3)
        draw = FreehandRectangle(text,margin=0.2,partitions=30,color=RED,fill_opacity=0.3)
        self.play(DrawBorderThenFill(draw),FadeInFromDirections(text[0]))
        self.wait()

class Test4(Scene):
    def construct(self):
        text = FunText(r"Alexander").scale(3)
        draw = FreehandRectangle(text,margin=0.2,partitions=30,color=RED,fill_opacity=0.3)
        self.play(DrawBorderThenFill(draw),FadeInFromRandom(text[0]))
        self.wait()

class Test5(Scene):
    def construct(self):
        text = FunText(r"Alexander").scale(3)
        draw = FreehandRectangle(text,margin=0.2,partitions=30,color=RED,fill_opacity=0.3)
        self.play(LagAnim(DrawBorderThenFill,text[0]))
        self.Oldplay(Escribe(text[0]))
        self.wait()

class Zig(Scene):
    def construct(self):
        path = TextMobject("Hola mundo a todos").scale(2)
        draw = ZigZag(path,color=RED,stroke_width=10)
        self.add(path)
        self.play(ShowCreation(draw,run_time=1,rate_func=linear))
        self.wait()

class JustifyScene(Scene):
    def construct(self):
        text = TextJustify(r"""\ECFAugie
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
            """,j_width=6,tex_template="tex_template_fonts.tex").scale(0.5)
        self.add(text)

class TestTime(Scene):
    def construct(self):
        c = Circle()
        s = Square()
        l = Line(DOWN,UP)
        time = DecimalNumber(self.time).add_updater(lambda m: m.set_value(self.time))
        time.to_corner(DL)
        self.add(time)
        self.play(
            # 6 partitions, that is (total_time = 4):
            # ShowCreation starts at t=0 and end t=(2/6)*total_time=1.333s
            ShowCreation(c,  rate_func=Custom(6,0,2)),
            # FadeIn starts at t=1.3333s and end t=(4/6)*total_time=2.6666s
            FadeIn(s,        rate_func=Custom(6,2,4)),
            # GrowFromCenter starts at t=2.6666s and end t=(6/6)*total_time=4s
            GrowFromCenter(l,rate_func=Custom(6,4,6)),
            run_time=4 # <- total_time
            )
        self.wait()

class TestRow(Scene):
    def construct(self):
        text = TextJustify(r"""\ECFAugie
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam
            """,j_width=6,tex_template="tex_template_fonts.tex").scale(0.5)
        rows = text.get_rows()
        words = text.get_words()
        rows[-1].fade(1)
        colors = it.cycle([RED,BLUE,GREEN,TEAL,GOLD])
        for word in words:
            word.set_color(next(colors))
        rows[2].get_words(-1).set_color(PURPLE)
        rows[0].get_words().set_color(YELLOW)
        rows[3].get_words()[1:].set_color(PINK)
        self.add(text)



class Dots(Dot):
    relative_objects = VGroup()
    def add_relative_dot(self):
        dot = Dot(radius=1.2)
        dot.set_color(RED)
        dot.shift([1,1,0])
        dot.add_updater(get_update_relative(self[0],dot))
        self.relative_objects.add(dot)

class Dots2(Dots):
    def modify_colors(self):
        self.relative_objects.set_color(GREEN)

class RelativeScene(Scene):
    def construct(self):
        dot_main = Dot(color=BLUE).scale(3)
        dot_relative = Ellipse(color=RED).set_width(0.2)
        VGroup(dot_relative,dot_main).scale(1)
        dot_relative.shift([0.2,0.2,0])

        alpha_width = dot_main.get_width()/dot_relative.get_width()
        line_main_relative = Line(dot_main.get_center(),dot_relative.get_center())
        alpha_length = dot_main.get_width() / line_main_relative.get_length()
        unit_vector = line_main_relative.get_unit_vector()

        print("dot_main_height: \t",dot_main.get_width())
        print("dot_relative_height: \t",dot_relative.get_width())
        print("alpha_width: \t",alpha_width)
        print("alpha_length: \t",alpha_length)

        group_relative = VGroup(dot_main,dot_relative)

        dot_relative.add_updater(get_update_relative(dot_main,dot_relative))
        #group_relative.add_updater(update_dot_relative)
        #self.add(group_relative)
        self.add(dot_main,dot_relative)
        self.play(dot_main.set_width,1)
        self.play(dot_main.shift,LEFT*2)
        print("dot_main_height: \t",dot_main.get_width())
        print("dot_relative_height: \t",dot_relative.get_width())
        print("alpha_width: \t",dot_main.get_width()/dot_relative.get_width())
        print("alpha_length: \t",alpha_length)
        self.wait(4)

class RelativeScene2(Scene):
    def construct(self):
        dot = Dots2(radius=1)
        ell = Ellipse().scale(2)
        dot.add_relative_dot()
        dot.modify_colors()
        self.add(dot,ell)
        self.play(FadeIn(dot.relative_objects))
        self.play(dot.match_width,ell)
        self.wait()

def me():
    print("Me ejecuto")


class MusicTest(Scene):
    def construct(self):
        pentagram = Pentagram(height=2)
        note = Crotchet(6,pentagram)
        note2 = Minim(-7,pentagram,stem_direction=UP)
        al = AdditionalLineNote(note)
        self.add(pentagram,note,al,note2)
        alpha_additiona_line = pentagram.get_space_between_lines() / al.get_width()
        pentagram.add_additional_line(-3,fade=1)
        pentagram.add_additional_line(2,0.5,fade=1)
        pentagram.additional_lines.set_stroke(opacity=0.5)
        #minim.put_note_at(0,0.3)
        #self.wait()
        note2.add_alteration("sharp")
        note2.alteration.fade(0.5)
        self.play(note2.set_note,7,0.5)
        self.wait()

class MusicTest3(Scene):
    def construct(self):
        pentagram = Pentagram(width=7,height=1.4)
        minim = Minim(0,pentagram)
        print(minim.get_note())
        sign = -1
        minim.set_note(sign*3)
        print(minim.get_note())
        minim.set_note(sign*2)
        print(minim.get_note())
        minim.set_note(sign*5)
        print(minim.get_note())
        minim.set_note(sign*0)
        print(minim.get_note())

class MusicTest2(Scene):
    def construct(self):
        pentagram = Pentagram(height=1)
        pentagram.add_key_signature("sharp",2)
        chord = ChordMobject(
                    Minim(0,pentagram,"bemol"),
                    Minim(3,pentagram,"sharp",stem_direction=UP)
                )
        chord.set_proportion(0.3)
        chord[0].add_alteration("sharp")
        self.add(pentagram,chord)
        self.play(chord[0].alteration.set_color,RED)
        self.wait()
        self.play(
            chord.set_notes,[-2,0],0.4,
            chord.set_color,RED
            )
        self.play(
            chord.set_notes,[-1,4],0.6,
            chord.set_color,ORANGE
            )
        self.play(
            chord.set_notes,[1,1],0.8,
            chord.set_color,TEAL
            )
        self.wait(2)
        #minim.put_note_at(0,0.3)
        #self.wait()
        #self.play(minim.set_note,2)

class MusicTest4(Scene):
    def construct(self):
        pentagram = Pentagram(height=2)
        chord = ChordMobject(
                    Minim(0,pentagram,"bemol"),
                    Minim(3,pentagram,"sharp",stem_direction=UP)
                )
        chord.set_proportion(0.3)

        self.add(pentagram,chord)
        chord[0].clear_updaters()
        self.play(chord[0].alteration.shift,RIGHT*2)
        chord[0].resume_updaters()
        self.wait()
        self.play(
            chord.set_notes,[-2,0],0.4,
            chord.set_color,RED
            )
        self.play(
            chord.set_notes,[-1,4],0.6,
            chord.set_color,ORANGE
            )
        self.play(
            chord.set_notes,[1,1],0.8,
            chord.set_color,TEAL
            )
        self.wait(2)

class AlterationAlphas(Scene):
    def construct(self):
        bemol,body,stem = SVGMobject("music_symbols/bemol_extra")
        self.add(bemol,body)
        reference_line = Line(body.get_center(),bemol.get_center())
        length = reference_line.get_length()
        ALPHA_BEMOL_SCALE = body.get_width() / bemol.get_width()
        UNIT_VECTOR_BEMOL = reference_line.get_unit_vector()
        ALPHA_BEMOL_LENGTH_VECTOR = body.get_width() / length
        print("ALPHA_BEMOL_SCALE: ",ALPHA_BEMOL_SCALE)
        print("UNIT_VECTOR_BEMOL: ",UNIT_VECTOR_BEMOL)
        print("ALPHA_BEMOL_LENGTH_VECTOR: ",ALPHA_BEMOL_LENGTH_VECTOR)

class AlterationObjects(Scene):
    def construct(self):
        flat = FormulaFull("\\flat")
        natural = FormulaFull("\\natural")
        sharp = FormulaFull("\\sharp")
        self.add(flat)

class BemolAlphas(Scene):
    def construct(self):
        self.bemol = MusicTeX(r"""
        \hsize=120mm
        \parindent 2pt
        \nostartrule
        \NOTes\qu{_e}\en
        """,stroke_width=0,stroke_opacity=0)

        self.bemol.symbol = self.bemol[0][0]
        self.bemol.stem = self.bemol[0][1]
        self.bemol.body = self.bemol[0][2]

        self.sharp = MusicTeX(r"""
        \hsize=120mm
        \parindent 2pt
        \nostartrule
        \NOTes\qu{^e}\en
        """,stroke_width=0,stroke_opacity=0)

        self.sharp.symbol = self.sharp[0][0]
        self.sharp.stem = self.sharp[0][1]
        self.sharp.body = self.sharp[0][2]

        self.natural = MusicTeX(r"""
        \hsize=120mm
        \parindent 2pt
        \nostartrule
        \NOTes\qu{=e}\en
        """,stroke_width=0,stroke_opacity=0)

        self.natural.symbol = self.natural[0][0]
        self.natural.stem = self.natural[0][1]
        self.natural.body = self.natural[0][2]

        self.notes = VGroup(self.bemol,self.sharp,self.natural).arrange(RIGHT)
        self.add(self.notes)

        self.get_alphas(self.natural)

    def get_alphas(self,object):
        body_width = object.body.get_width()
        stem_width = object.stem.get_width()
        stem_height = object.stem.get_height()
        symbol_width = object.symbol.get_width()
        reference_line_symbol = Line(
            object.body.get_center(),
            object.symbol.get_center(),
            buff=0
            )
        reference_line_stem = Line(
            object.body.get_center(),
            object.stem.get_center()
        )
        unit_vector_symbol = reference_line_symbol.get_unit_vector()
        unit_vector_stem = reference_line_stem.get_unit_vector()
        vector_length_symbol = reference_line_symbol.get_length()
        vector_length_stem = reference_line_stem.get_length()

        alphas = {
            "alpha_width_symbol":body_width/symbol_width,
            "alpha_width_stem":body_width/stem_width,
            "alpha_height_stem":body_width/stem_height,
            "alpha_vector_length_symbol":body_width/vector_length_symbol,
            "alpha_vector_length_stem":body_width/vector_length_stem,
            "unit_vector_symbol":unit_vector_symbol,
            "unit_vector_stem":unit_vector_stem,
        }

        print(alphas)

class GetNotes(Scene):
    def construct(self):
        kwargs = {
            "stroke_width":0,
            "stroke_opacity":0,
            "fill_opacity":1
        }
        crotchet = self.natural = MusicTeX(r"""
        \hsize=120mm
        \parindent 2pt
        \nostartrule
        \NOTes\qa{e}\en
        """,**kwargs)

        minim = MusicTeX(r"""
        \hsize=120mm
        \parindent 2pt
        \nostartrule
        \NOTes\ha{e}\en
        """,**kwargs)

        semibreve = MusicTeX(r"""
        \hsize=120mm
        \parindent 2pt
        \nostartrule
        \NOTes\wh{e}\en
        """,**kwargs)

        self.add(crotchet)

class Alteraciones(Scene):
    def construct(self):
        alteraciones_sostenidos = MusicTeX(r"""
            \hsize=100mm
            \generalsignature{7}
            \startpiece\bigaccid
            """)
        alteraciones_bemoles = MusicTeX(r"""
            \hsize=100mm
            \generalsignature{-7}
            \startpiece\bigaccid
            """)
        alteraciones = VGroup(alteraciones_bemoles,alteraciones_sostenidos).arrange(DOWN)
        self.add(alteraciones)

class GetAlteraciones(Scene):
    def construct(self):
        sostenidos = SVGMobject("music_symbols/key_signature_sharp")
        bemoles = SVGMobject("music_symbols/key_signature_bemol")
        lineas_sostenidos = sostenidos[:5].set_color(RED)
        alteraciones_sostenidos = sostenidos[7:].set_color(GREEN)
        lineas_bemoles = bemoles[:5].set_color(RED)
        alteraciones_bemoles = bemoles[7:].set_color(GREEN)

        alpha_width_kss = lineas_sostenidos.get_height() / alteraciones_sostenidos.get_width()
        alpha_width_ksb = lineas_bemoles.get_height() / alteraciones_bemoles.get_width()

        dy_kss = alteraciones_sostenidos.get_y()-lineas_sostenidos.get_y()
        dy_kss_alpha = alteraciones_sostenidos.get_width() / dy_kss

        dy_ksb = alteraciones_bemoles.get_y()-lineas_bemoles.get_y()
        dy_ksb_alpha = alteraciones_bemoles.get_width() / dy_ksb

        alphas = {
            "kss": {
                "width":alpha_width_kss,
                "dy": dy_kss_alpha
            },
            "ksb": {
                "width":alpha_width_ksb,
                "dy": dy_ksb_alpha
            }
        }

        group = VGroup(sostenidos,bemoles).arrange(DOWN)
        group.shift(RIGHT)
        self.add(group)
        print(alphas)

class ArmaduraSostenido(CheckSVG):
    CONFIG = {
        "file":"music_symbols/key_signature_sharp",
        "show_numbers":True
    }

class ArmaduraBemol(CheckSVG):
    CONFIG = {
        "file":"music_symbols/key_signature_bemol",
        "show_numbers":True
    }